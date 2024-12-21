from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('update_status')
def handle_status_update(data):
    status = data.get('status')
    vehicle_speeds = data.get('vehicle_speeds', {})
    timestamp = data.get('timestamp')
    location = data.get('location')

    print(f"Status: {status}")
    print(f"Vehicle Speeds: {vehicle_speeds}")
    print(f"Timestamp: {timestamp}")
    print(f"Location: {location}")
    
    emit('status_update', {
        'status': status,
        'vehicle_speeds': vehicle_speeds,
        'timestamp': timestamp,
        'location': location
    }, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)