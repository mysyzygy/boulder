from app import db
from sqlalchemy import select
from app.models import Order, Ticker
import numpy as np

class Strategy:
    def __init__(self, portfolio):
        self.portfolio = portfolio
        self.db = db

    def get_prices(self, window):
        return db.session.query(Ticker).order_by(Ticker.date.desc()).limit(
            window).all()

    def analyze(self, data):
        prices = self.get_prices(10)
        close_prices = np.array([price.close for price in prices])
        trend = np.sum(np.diff(close_prices))
        if trend > 5:
            self.portfolio.buy(symbol=data.symbol, price=data.close, shares=10)
        elif trend < -5:
            self.portfolio.sell(symbol=data.symbol, price=data.close,
                                shares=10)

