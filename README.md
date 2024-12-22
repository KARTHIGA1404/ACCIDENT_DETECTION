#**CODE IS KUMARAGURU COLLEGE OF TECHNOLOGY'S ASSESTS**

**Accident Detection with Speed Detection**

**Project Description**

This project implements a real-time system for detecting vehicle accidents with speed detection as a feature. It uses video processing to monitor vehicle speeds, identify collisions, and send alerts to a website with details of the incident, including timestamp, location, and speeds of involved vehicles.

---

**Features**

1. **Vehicle Detection and Tracking**
2. **Speed Calculation of Vehicles**
3. **Accident Detection through Collision Analysis**
4. **Real-time Alert Sending to Web Interface**

---

**Prerequisites**

1. **Python (3.x)**
2. **Libraries:**
   - Flask
   - Flask-SocketIO
   - OpenCV
   - NumPy
   - SocketIO
3. **Software:**
   - Any IDE or text editor (e.g., VS Code, PyCharm)
   - A video file (e.g., `cr.mp4` for testing)
4. **Browser:**
   - To view the real-time web interface

---

**Installation Steps**

1. Set Up Python Environment

Ensure Python is installed. You can download it from [Python.org](https://www.python.org/).

2. Install Required Libraries

Run the following commands in the terminal or command prompt:

```bash
pip install flask flask-socketio opencv-python numpy python-socketio
```

3. Clone or Copy the Project

Clone this repository or copy the project files into your workspace.

4. Add Video File

Place your video file (e.g., `cr.mp4`) in the project directory.

---

**Project Structure**

```
AccidentDetectionProject/
├── app.py
├── main.py
├── templates/
│   └── index.html
├── static/
│   └── cr.mp4
```

- `app.py`: Backend server with Flask and SocketIO.
- `main.py`: Main script for video processing and accident detection.
- `templates/index.html`: Frontend interface.
- `static/cr.mp4`: Video file for testing.

---

Running the Project

1. Start the Backend Server

Run the Flask app to start the server:

```bash
python app.py
```

The server will run on `http://127.0.0.1:5000`.

2. Open Web Interface

Open a browser and navigate to `http://127.0.0.1:5000` to view the real-time status updates.

3. Run the Main Script

Run the video processing script to start monitoring:

```bash
python main.py
```

4. View Alerts

Accidents and vehicle speeds will be displayed in the browser in real-time.

---

**How It Works**

1. **Video Processing:** The system reads video frames and detects vehicles using contour detection.
2. **Speed Calculation:** Tracks vehicle positions between frames to calculate speeds.
3. **Accident Detection:** Detects collisions and triggers alerts after verifying sustained contact.
4. **Real-time Updates:** Sends accident data to the web interface using SocketIO.

---

**Example Alerts**

- Status: `Accident Detected!`
- Vehicle Speeds: `{Vehicle 0: 15.2 m/s, Vehicle 1: 13.4 m/s}`
- Timestamp: `2024-12-22 15:30:45`
- Location: `Latitude: 12.9716, Longitude: 77.5946`

---

**Troubleshooting**

- **Error: Could not open video file**: Ensure `cr.mp4` is in the correct directory.
- **SocketIO connection issue**: Check if the server is running and accessible.
- **No accident detection**: Test with different video files.

---

**Future Enhancements**

1. Improve vehicle detection using YOLO or other advanced object detection models.
2. Integrate GPS for dynamic location tracking.
3. Extend alert system to send SMS or emails.

---


