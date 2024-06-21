from app import create_app
from data import polygon_helper
import threading
from flask_socketio import SocketIO

import logging
logging.getLogger().addHandler(logging.StreamHandler())
logging.getLogger().setLevel(logging.DEBUG)

app = create_app()

if __name__ == '__main__':
    # socketio = SocketIO(app)
    print("Starting websocket server...")
    t1 = threading.Thread(target=polygon_helper.run_client,
                          args=("XAS.BTC-USD",))
    t1.start()
    app.run(host='0.0.0.0', debug=True)
    t1.join()
