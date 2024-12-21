import cv2
import numpy as np
from socketio import Client
from datetime import datetime

# Initialize SocketIO client
socketio = Client()
try:
    socketio.connect('http://127.0.0.1:5000')
    print("Successfully connected to server")
except Exception as e:
    print(f"Failed to connect to server: {e}")
    exit(1)

def send_alert_to_website(status, speeds, timestamp, location):
    socketio.emit('update_status', {
        'status': status,
        'vehicle_speeds': speeds,
        'timestamp': timestamp,
        'location': location
    })

def calculate_speed(prev_center, current_center, frame_interval, scale_factor=0.05):
    """Calculate speed of vehicle in meters per second"""
    distance = np.linalg.norm(np.array(current_center) - np.array(prev_center)) * scale_factor
    return distance / frame_interval

def detect_crash(vehicles, collision_frames, tracked_speeds):
    """
    Detect collisions between vehicles and return colliding vehicles' speeds
    """
    for i in range(len(vehicles)):
        for j in range(i + 1, len(vehicles)):
            x1, y1, x2, y2 = vehicles[i]
            x3, y3, x4, y4 = vehicles[j]

            # Check for collision
            if x1 < x4 and x3 < x2 and y1 < y4 and y3 < y2:
                key = f"collision_{i}_{j}"
                collision_frames[key] = collision_frames.get(key, 0) + 1
                
                if collision_frames[key] > 5:
                    # Get speeds of colliding vehicles
                    speed1 = tracked_speeds.get(i, 0)
                    speed2 = tracked_speeds.get(j, 0)
                    return True, {
                        f"Vehicle {i}": f"{speed1:.2f} m/s",
                        f"Vehicle {j}": f"{speed2:.2f} m/s"
                    }
            else:
                collision_frames[f"collision_{i}_{j}"] = 0

    return False, {}

def main():
    video_path = "cr.mp4"
    video_capture = cv2.VideoCapture(video_path)

    if not video_capture.isOpened():
        print(f"Error: Could not open video file '{video_path}'.")
        return

    prev_frame = None
    cv2.namedWindow("Vehicle Monitoring System", cv2.WINDOW_NORMAL)

    fps = video_capture.get(cv2.CAP_PROP_FPS)
    frame_interval = 1 / fps
    tracked_vehicles = {}
    collision_frames = {}
    
    while True:
        ret, frame = video_capture.read()
        if not ret:
            break

        frame = cv2.resize(frame, (1020, 500))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5, 5), 0)

        if prev_frame is not None:
            frame_delta = cv2.absdiff(prev_frame, gray)
            thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]
            thresh = cv2.dilate(thresh, None, iterations=2)

            contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            detected_vehicles = []
            tracked_speeds = {}

            for contour in contours:
                if cv2.contourArea(contour) < 500:
                    continue

                x, y, w, h = cv2.boundingRect(contour)
                center = (x + w // 2, y + h // 2)
                detected_vehicles.append((x, y, x + w, y + h))

                # Track vehicle and calculate speed
                vehicle_id = len(tracked_speeds)
                if vehicle_id in tracked_vehicles:
                    prev_center = tracked_vehicles[vehicle_id]['center']
                    speed = calculate_speed(prev_center, center, frame_interval)
                    tracked_speeds[vehicle_id] = speed
                    
                    # Display speed on frame
                    cv2.putText(frame, f"ID:{vehicle_id} Speed:{speed:.2f} m/s", 
                              (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

                tracked_vehicles[vehicle_id] = {'center': center, 'bbox': (x, y, w, h)}
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Check for accidents
            accident_detected, collision_speeds = detect_crash(detected_vehicles, collision_frames, tracked_speeds)
            
            if accident_detected:
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                location = "Latitude: 12.9716, Longitude: 77.5946"
                
                # Display accident alert on frame
                cv2.putText(frame, f"Accident Detected! {timestamp}", 
                          (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                
                # Send alert with vehicle speeds
                send_alert_to_website("Accident Detected!", collision_speeds, timestamp, location)

        cv2.imshow("Vehicle Monitoring System", frame)
        prev_frame = gray

        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()
    socketio.disconnect()

if __name__ == "__main__":
    main()