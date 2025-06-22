# Write the README content into a Markdown (.md) file

readme_content = """
# GestureMediaPro 🎛️🖐️  
Real-time hand gesture controlled media player built with Python, OpenCV, and MediaPipe.

## 📌 What is GestureMediaPro?

GestureMediaPro lets you control media playback using your hands — no mouse, no keyboard.  
Show 1 to 5 fingers and control volume, play/pause, mute, and more, using just your webcam.

Ideal for touchless control while watching videos, listening to music, or during presentations.

## ⚙️ Features

✅ Real-time hand tracking using MediaPipe  
✅ Finger-count based gesture recognition (1–5 fingers)  
✅ Custom gesture-to-action mapping via GUI  
✅ Works with right or left hand  
✅ Clean project structure (modular & maintainable)

## 🧰 Technologies Used

| Technology   | What it does                                |
|--------------|---------------------------------------------|
| Python       | Core programming language                   |
| OpenCV       | Webcam input, image display & drawing       |
| MediaPipe    | Hand detection and landmark tracking        |
| PyAutoGUI    | Simulates keyboard presses (e.g., spacebar) |
| Tkinter      | GUI for mapping gestures to actions         |
| JSON         | Stores user preferences                     |

## 🖥️ How to Run Locally

1. Clone the repo:

```bash
git clone https://github.com/yourusername/GestureMediaPro.git
cd GestureMediaPro
