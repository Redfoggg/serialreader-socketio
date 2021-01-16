"""Timer module"""
import time
from flask_socketio import SocketIO, emit
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app, cors_allowed_origins="*")

app.debug = True
app.host = 'localhost'

positions = {
    5: 0,#"p1",
    15: 1,#"p2",
    25: 2,#"p3",
    50: 3#"p4"
}

@socketio.on("monitoring")
def serial_reader(machine_id):
    """Monitoring loop"""
    count = 0
    print(machine_id)
    while True:
        time.sleep(1)
        emit_position(positions.get(count, ""))
        count += 1
        print(count)


def emit_position(value):
    """Emit position information to client"""
    if not value:
        return
    print(value)
    emit("monitoring", value)

if __name__ == '__main__':
    socketio.run(app)
