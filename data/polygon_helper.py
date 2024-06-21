from polygon import WebSocketClient
from polygon.websocket.models import *
from typing import List
from app import db
from run import app
from app.models import Ticker
import datetime
from functools import partial

import logging
logging.getLogger().addHandler(logging.StreamHandler())
logging.getLogger().setLevel(logging.DEBUG)

client = WebSocketClient(market=Market.Crypto)  #
# POLYGON_API_KEY
# environment variable
# is used

def handle_msg(msgs: List[WebSocketMessage]):
    with app.app_context():
        for m in msgs:
            print(m)
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

            db.session.add(ticker)
            db.session.commit()
        # socketio.emit("price_event", ticker.to_json())


def run_client(symbols):
    client.subscribe(symbols)
    # g = partial(handle_msg, socketio)
    client.run(handle_msg)

# run_client()

#
#
# from polygon import WebSocketClient
# from polygon.websocket.models import WebSocketMessage
# from typing import List
# import asyncio
#
# c = WebSocketClient(subscriptions=["AM.TSLA"], feed=Feed.Delayed)
#
#
# async def handle_msg(msgs: List[WebSocketMessage]):
#     for m in msgs:
#         print(m)
#
#
# async def timeout():
#     await asyncio.sleep(1200)
#     print("unsubscribe_all")
#     c.unsubscribe_all()
#     await asyncio.sleep(1)
#     print("close")
#     await c.close()
#
#
# async def main():
#     print("starting async")
#     await asyncio.gather(c.connect(handle_msg), timeout())
#
#
# asyncio.run(main())