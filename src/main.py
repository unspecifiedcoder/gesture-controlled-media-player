import cv2
import mediapipe as mp
import pyautogui
import time
import math

# MediaPipe setup
cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
draw = mp.solutions.drawing_utils

# Timing
last_action = 0
COOLDOWN = 0.8

# Pinch tracking
pinch_start_time = None
pinch_start_x = None

def can_trigger():
    global last_action
    now = time.time()
    if now - last_action > COOLDOWN:
        last_action = now
        return True
    return False

def distance(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    gesture = "NONE"

    if result.multi_hand_landmarks:
        hand = result.multi_hand_landmarks[0]
        draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)
        lm = hand.landmark

        thumb = lm[4]
        index = lm[8]
        wrist = lm[0]

        pinch_dist = distance(thumb, index)

        # 🤏 PINCH ACTIVE
        if pinch_dist < 0.045:
            if pinch_start_time is None:
                pinch_start_time = time.time()
                pinch_start_x = wrist.x

            # ⏯ PLAY / PAUSE (pinch held still)
            elif time.time() - pinch_start_time > 1.0 and can_trigger():
                pyautogui.press("playpause")
                gesture = "PLAY / PAUSE"
                pinch_start_time = None

            # 👉👈 SEEK (pinch + move)
            dx = wrist.x - pinch_start_x
            if dx > 0.18 and can_trigger():
                pyautogui.press("right")   # +10s YouTube
                gesture = "+10 SECONDS"
                pinch_start_time = None
            elif dx < -0.18 and can_trigger():
                pyautogui.press("left")    # -10s YouTube
                gesture = "-10 SECONDS"
                pinch_start_time = None

        else:
            pinch_start_time = None
            pinch_start_x = None

            # 🔊 VOLUME CONTROL (pinch open / close)
            if pinch_dist > 0.085 and can_trigger():
                pyautogui.press("volumeup")
                gesture = "VOLUME UP"
            elif pinch_dist < 0.06 and can_trigger():
                pyautogui.press("volumedown")
                gesture = "VOLUME DOWN"

    cv2.putText(
        frame,
        f"Gesture: {gesture}",
        (10, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2,
    )

    cv2.imshow("Gesture Media Control", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
