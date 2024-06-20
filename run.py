from app import create_app
from data import polygon_helper
import threading
from flask_socketio import SocketIO

app = create_app()

if __name__ == '__main__':
    socketio = SocketIO(app)
    print("Starting websocket server...")
    t1 = threading.Thread(target=polygon_helper.run_client,
                          args=("APPL", socketio))
    t1.start()
    socketio.run(app=app, host='0.0.0.0', debug=True, allow_unsafe_werkzeug=True)
    t1.join()
