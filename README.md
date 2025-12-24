# Gesture Controlled Media Player 🎥✋

A real-time hand gesture–based media control system built using **MediaPipe**, **OpenCV**, and **PyAutoGUI**.  
This project allows users to control media playback (such as **YouTube videos in the browser**) using simple and reliable hand gestures captured through a webcam.

The focus of this project is **robustness and usability**, avoiding complex or fragile gesture recognition techniques.

---

## 🚀 Features

### 🔊 Volume Control
- 🤏 **Pinch fingers close** → Volume Down
- 🤏 **Pinch fingers apart** → Volume Up

### ⏯ Play / Pause
- 🤏 **Pinch and hold the hand steady for ~1 second** → Toggle Play / Pause

### ⏩ Video Seek (YouTube)
- 🤏 **Pinch + move hand right** → Skip forward 10 seconds
- 🤏 **Pinch + move hand left** → Rewind 10 seconds

> All gestures are intentionally based on **pinch distance, time, and hand movement**, which are the most stable signals provided by MediaPipe.

---

## 🧠 How It Works

1. The webcam feed is captured using **OpenCV**
2. **MediaPipe Hands** detects 21 hand landmarks in real time
3. Gesture logic is derived from:
   - Distance between thumb and index finger (pinch)
   - Time (for hold-based actions)
   - Horizontal hand movement (for seek control)
4. Media actions are executed using **system media keys** via **PyAutoGUI**
5. This approach works seamlessly with browser-based media players like **YouTube**

---

## 🛠 Tech Stack

- **Python 3.9**
- OpenCV
- MediaPipe
- PyAutoGUI

---

## 📁 Project Structure

```
gesture-spotify-control/
│
├── src/
│   ├── main.py        # Main application logic
│   └── gestures.py    # Gesture utility functions
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/gesture-spotify-control.git
cd gesture-spotify-control
```

### 2️⃣ Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

1. Open **YouTube** in your browser and play any video
2. Run the application:
```bash
python src/main.py
```
3. Perform gestures in front of the webcam

Press **ESC** to exit the program.

---

## 🧪 Gesture Usage Guide

| Gesture | Action |
|------|------|
| 🤏 Pinch close | Volume Down |
| 🤏 Pinch open | Volume Up |
| 🤏 Pinch + hold (1s) | Play / Pause |
| 🤏 Pinch + move right | +10 seconds |
| 🤏 Pinch + move left | −10 seconds |

---

## 📌 Notes

- Designed for **Windows OS**
- Requires a working webcam
- Works best under good lighting conditions
- Gestures are intentionally minimal to reduce false triggers

---

## 🚧 Future Improvements

- Gesture calibration mode
- On-screen gesture guide
- Spotify Web API integration
- Cross-platform (Linux/macOS) support
- Smoother analog volume control

---

## 👤 Author

**RAVI SHANKAR BEJINI**
