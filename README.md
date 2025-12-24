# Gesture Controlled Media Player 🎥✋

A real-time hand gesture–based media control system built using **MediaPipe**, **OpenCV**, and **PyAutoGUI**.  
This project allows users to control media playback (YouTube, browser media, etc.) using intuitive hand gestures captured via a webcam.

---

## 🚀 Features

- 🤏 **Pinch Gesture**
  - Pinch close → Volume Down
  - Pinch open → Volume Up
- ⏯ **Play / Pause**
  - Pinch and hold still for 1 second
- ⏩ **Seek Control (YouTube)**
  - Pinch + move hand right → +10 seconds
  - Pinch + move hand left → −10 seconds
- Real-time hand landmark tracking
- Works on browser-based media players (YouTube, Spotify Web, etc.)

---

## 🧠 How It Works

1. Webcam feed is captured using OpenCV
2. MediaPipe detects 21 hand landmarks in real time
3. Gesture logic is computed using:
   - Thumb–index distance (pinch)
   - Time (hold detection)
   - Horizontal hand movement (seek)
4. Media actions are triggered using system media keys via PyAutoGUI

---

## 🛠 Tech Stack

- Python 3.9
- OpenCV
- MediaPipe
- PyAutoGUI

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/gesture-spotify-control.git
cd gesture-spotify-control
