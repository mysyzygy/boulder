from analysis.Strategy import Strategy
from analysis.portfolio import Portfolio

from app import create_app
from data import polygon_helper
from threading import Thread
from flask_socketio import SocketIO

import logging
logging.getLogger().addHandler(logging.StreamHandler())
logging.getLogger().setLevel(logging.DEBUG)

app = create_app()
socketio = SocketIO(app,  async_mode='threading', logger=True)

portfolio = Portfolio(socketio, cash=100000)
strategy = Strategy(socketio)

@socketio.on('connected')
def handle_my_custom_event(json):
    logging.debug('RECEIVED CONNECTED EVENT!!!')


@socketio.on("special")
def handle_price_event(data):
    logging.debug('RECEIVED PRICE EVENT!!!!')
    strategy.analyze(data)


print("Starting websocket server...")
socketio.start_background_task(polygon_helper.run_client,
            "XAS.BTC-USD", app, socketio)  # Aggregate Seconds
            # "XA.BTC-USD", app, socketio)     # Aggregate Minutes

if __name__ == '__main__':
    socketio.run(app=app, debug=True, use_reloader=False)


