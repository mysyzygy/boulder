from polygon import WebSocketClient
from polygon.websocket.models import WebSocketMessage
from typing import List
from app import db
from app.models import Ticker
import datetime
client = WebSocketClient()  # POLYGON_API_KEY environment variable is used

def handle_msg(msgs: List[WebSocketMessage]):
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


def run_client(ticker):
    client.subscribe(f"AM.{ticker}")
    client.run(handle_msg)
