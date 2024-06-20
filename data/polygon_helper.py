from polygon import WebSocketClient
from polygon.websocket.models import WebSocketMessage
from typing import List
from app import db
from app.models import Ticker
import datetime
from functools import partial
client = WebSocketClient()  # POLYGON_API_KEY environment variable is used

def handle_msg(socketio, msgs: List[WebSocketMessage]):
    for m in msgs:
        print(m)
        ticker = Ticker(
            name=m.get("sym"),
            date=datetime.datetime.fromtimestamp(m.get("s")),
            open=m.get("o"),
            high=m.get("h"),
            low=m.get("l"),
            close=m.get("c"),
            volume=m.get("v"),
        )

        db.session.add(ticker)
        db.session.commit()
        socketio.emit("price_event", ticker.to_json())


def run_client(ticker, socketio):
    client.subscribe(f"AM.{ticker}")
    g = partial(handle_msg, socketio)
    client.run(g)
