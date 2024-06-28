from datetime import datetime
from app import db
from app.models import Order, Ticker

from sqlalchemy import select
import logging

class Portfolio:
    def __init__(self, app, cash):
        self.cash = cash
        self.app = app
        self.db = db
        self.id_ctr = self.get_latest_order_id() + 1

    def get_latest_order_id(self):
        with self.app.app_context():
            try:
                result = self.db.session.query(Order).order_by(Order.id.desc(
                )).limit(
                    1).all()
                return result[0].id
            except Exception as e:
                return 0


    def buy(self, symbol, price, shares):
        logging.info("BUY ORDER RECEIVED!!!")
        date = datetime.now()
        order = Order(
            id=self.id_ctr,
            symbol=symbol,
            date=date,
            shares=shares,
            price=price,
            transaction="buy"
        )
        self.db.session.add(order)
        self.db.session.commit()
        self.cash -= price * shares
        self.id_ctr += 1
        logging.info(f"Cash Balance: {self.cash}")

    def sell(self, symbol, price, shares):

        logging.info("SELL ORDER RECEIVED!!!")
        date = datetime.now()
        order = Order(
            id=self.id_ctr,
            symbol=symbol,
            date=date,
            shares=shares,
            price=price,
            transaction="sell"
        )
        self.db.session.add(order)
        self.db.session.commit()
        self.cash += price * shares
        self.id_ctr += 1
        logging.info(f"Cash Balance: {self.cash}")

    def get_orders(self, amount=10):
        orders = self.db.execute(select(Order).order_by("id", reversed).limit(
            amount))
        return orders