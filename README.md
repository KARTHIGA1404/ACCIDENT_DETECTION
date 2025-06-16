# **🚗 Vehicle Accident Detection & Real-Time Alert System**

---

## 🔍 Project Overview

This Python-based system detects vehicle movement from video feeds, calculates their speeds, and identifies potential accidents by detecting collisions. Once a collision is confirmed, it sends real-time alerts to a Flask web interface via SocketIO, including vehicle speeds, timestamp, and location details.

---

## 📂 Project Structure

```
vehicle_alert_system/
├── app.py  # Flask server with SocketIO 
├── main.py # Vehicle tracking & alert script 
├── templates/
│   └── index.html   # Web UI 
├── cr.mp4                                    # Input video for vehicle monitoring
└── README.md                                 # Project documentation
```

> 💡 Rename the `.py` and `.html` files meaningfully as shown for better clarity in your repo.

---

## 🔧 Requirements

* Python 3.x
* OpenCV
* NumPy
* Flask
* Flask-SocketIO
* python-socketio (for client)

### 📦 Install Dependencies

```bash
pip install opencv-python numpy flask flask-socketio "python-socketio[client]"
```

---

## ▶️ How to Run

1. Ensure `cr.mp4` is present in the project directory.
2. Run the Flask server:

```bash
python app.py  # (rename 6ea7... to app.py)
```

3. In a new terminal, start the vehicle monitoring script:

```bash
python vehicle_monitor.py  # (rename 78e1... to vehicle_monitor.py)
```

4. Open `http://127.0.0.1:5000` in your browser to view the alert dashboard.

---

## ⚙️ How It Works

* Reads frames from the input video (`cr.mp4`).
* Applies motion detection to locate moving vehicles.
* Tracks vehicle positions and estimates their speeds.
* Checks for overlapping bounding boxes (potential collisions).
* If a collision persists for >5 frames:

  * Calculates and sends speeds of involved vehicles.
  * Displays an alert with timestamp and location on the web UI via SocketIO.

---

## 🧠 Key Features

* Real-time vehicle speed estimation
* Collision detection using bounding box overlaps
* Flask-based live dashboard
* SocketIO-powered instant communication
* Alerts include speed, time, and location

---

## 📌 Parameters

* `scale_factor = 0.05`: Assumed pixel-to-meter ratio
* `collision_frames[key] > 5`: Frame persistence threshold to confirm a crash
* `video_path = "cr.mp4"`: Input video path
* `location = "Latitude: 12.9716, Longitude: 77.5946"`: Static geolocation (can be updated)

---

## 📈 Output

* Console shows detection progress and crash info
* Web dashboard displays:

  * System status (monitoring/crash)
  * Timestamp and geolocation
  * Vehicle speeds during crash

---
## 📸 Output Frame Example

![Screenshot 2025-06-16 155925](https://github.com/user-attachments/assets/40e40148-cf64-4f5f-b403-7ef2ac3312c7)
![Screenshot (706)](https://github.com/user-attachments/assets/3aa16f50-5b16-40b0-95d0-6a7d6ea86c21)
![Screenshot 2025-06-16 160044](https://github.com/user-attachments/assets/b5e29c6e-b116-4b9e-a2b7-ac3d709b7c8e)

---
### 📌
### The above accident detection is one part of this comprehensive project. 
The Accident Detection and Alert System is a real-time AI-powered solution that identifies road accidents, detects overspeeding vehicles, and recognizes victims using facial recognition technology. By analyzing live or recorded CCTV footage with computer vision models, the system detects incidents instantly and sends alert messages containing the date, time, and exact location to the nearest police station or emergency contact. It maintains privacy by not storing any personal data and dynamically manages traffic flow during emergencies by counting vehicles in all directions and adjusting traffic signals accordingly. This intelligent system enhances road safety, accelerates emergency response, and supports effective traffic management. 
