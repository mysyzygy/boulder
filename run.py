

from app import create_app
from app.data import polygon_helper
from threading import Thread
from flask_socketio import SocketIO

import logging
logging.getLogger().addHandler(logging.StreamHandler())
logging.getLogger().setLevel(logging.INFO)

app = create_app()
socketio = SocketIO(app,  async_mode='threading',
                    logger=True
                    )


@socketio.on('connected')
def handle_my_custom_event(json):
    logging.debug('RECEIVED CONNECTED EVENT!!!')


@socketio.on("special_price_event")
def handle_price_event(data):
    logging.debug('RECEIVED PRICE EVENT!!!!')



print("Starting websocket server...")
socketio.start_background_task(polygon_helper.run_client,
            "XAS.BTC-USD", app, socketio)  # Aggregate Seconds
            # "XA.BTC-USD", app, socketio)     # Aggregate Minutes

if __name__ == '__main__':
    socketio.run(app=app, debug=True, use_reloader=False, allow_unsafe_werkzeug=True)


