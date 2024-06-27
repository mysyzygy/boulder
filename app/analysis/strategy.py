from app import db
from sqlalchemy import select
from app.models import Order, Ticker
import numpy as np

class Strategy:
    def __init__(self, socketio):
        self.socketio = socketio
        self.db = db

    def get_prices(self, window):
        return db.session.query(Ticker).order_by(Ticker.date.desc()).limit(
            window).all()


    def analyze(self):
        prices = self.get_prices(10)
        close_prices = np.array([price.close for price in prices])
        trend = np.sum(np.diff(close_prices))
        if trend > 5:
            self.socketio.emit('buy_order', prices[0].to_json())
            self.socketio.sleep(0)
        elif trend < -5:
            self.socketio.emit('sell_order', prices[0].to_json())
            self.socketio.sleep(0)

