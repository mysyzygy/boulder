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

socketio.run(app=app, host='0.0.0.0', use_reloader=False)
t1.join()
