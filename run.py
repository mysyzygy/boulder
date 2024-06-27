from app.analysis.strategy import Strategy
from app.analysis.portfolio import Portfolio

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

portfolio = Portfolio(socketio, cash=100000)
strategy = Strategy(socketio)

@socketio.on('connected')
def handle_my_custom_event(json):
    logging.debug('RECEIVED CONNECTED EVENT!!!')


@socketio.on("special_price_event")
def handle_price_event(data):
    logging.debug('RECEIVED PRICE EVENT!!!!')
    strategy.analyze()


@socketio.on("special_buy_order")
def handle_buy_event(data):
    logging.info('RECEIVED BUY ORDER EVENT!!!!')
    portfolio.buy(data)


@socketio.on("special_sell_order")
def handle_sell_event(data):
    logging.info('RECEIVED SELL ORDER EVENT!!!!')
    portfolio.sell(data)



print("Starting websocket server...")
socketio.start_background_task(polygon_helper.run_client,
            "XAS.BTC-USD", app, socketio)  # Aggregate Seconds
            # "XA.BTC-USD", app, socketio)     # Aggregate Minutes

if __name__ == '__main__':
    socketio.run(app=app, debug=True, use_reloader=False)


