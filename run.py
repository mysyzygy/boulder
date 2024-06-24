from app import create_app
from data import polygon_helper
from threading import Thread
from flask_socketio import SocketIO
import time

import logging
logging.getLogger().addHandler(logging.StreamHandler())
logging.getLogger().setLevel(logging.INFO)

app = create_app()
socketio = SocketIO(app)


print("Starting websocket server...")
t1 = Thread(target=polygon_helper.run_client,
                      args=("XAS.BTC-USD", app, socketio))
t1.start()
if __name__ == '__main__':
    socketio.run(app=app, debug=True, use_reloader=False)
t1.join()
