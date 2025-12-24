import math
import time

last_time = 0
COOLDOWN = 1.0

def distance(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def can_trigger():
    global last_time
    now = time.time()
    if now - last_time > COOLDOWN:
        last_time = now
        return True
    return False

def is_open_palm(lm):
    return (
        lm[8].y < lm[6].y and
        lm[12].y < lm[10].y and
        lm[16].y < lm[14].y and
        lm[20].y < lm[18].y
    )
