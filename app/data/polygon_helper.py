from random import random

from polygon import WebSocketClient

from typing import List
import sqlalchemy
from polygon.websocket.models.common import Market
from polygon.websocket.models.models import WebSocketMessage

from app import db
from app.models import Ticker
from app.analysis.strategy import Strategy
from app.analysis.portfolio import Portfolio

import datetime
from functools import partial
import logging


client = WebSocketClient(market=Market.Crypto)  #
# POLYGON_API_KEY
# environment variable
# is used


def handle_msg(app, socketio, strategy, msgs: List[WebSocketMessage]):
    with app.app_context():
        for m in msgs:
            s = m.end_timestamp / 1000.0
            time = datetime.datetime.fromtimestamp(s).strftime('%Y-%m-%d '
                                                             '%H:%M:%S.%f')

            ticker = Ticker(
                symbol_date_id=f"{m.pair}_{time}",
                symbol=m.pair,
                date=time,
                open=m.open,
                high=m.high,
                low=m.low,
                close=m.close,
                volume=m.volume,
            )
            try:
                db.session.add(ticker)
                db.session.commit()
            except sqlalchemy.exc.IntegrityError as e:
                logging.error(e)

            strategy.analyze(ticker)
            close = str(ticker.close)
            cash = str(
                strategy.portfolio.cash)
            socketio.emit("price_event", {"data": cash})
            socketio.sleep(0)



def run_client(symbols, app, socketio):
    client.subscribe(symbols)
    portfolio = Portfolio(app, cash=100000)
    strategy = Strategy(portfolio)
    f = partial(handle_msg, app, socketio, strategy)

    client.run(f)

