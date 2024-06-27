from datetime import datetime
from app import db
from app.models import Order
from sqlalchemy import select
import logging

class Portfolio:
    def __init__(self, socketio, cash):
        self.cash = cash
        self.db = db
        self.id_ctr = 0

    def buy(self, data):
        logging.info("BUY ORDER RECIEVED!!!")
        date = datetime.now()
        order = Order(self.id_ctr,
                      data["symbol"],
                      date,
                      data["shares"],
                      data["price"],
                      "buy")
        self.db.session.add(order)
        self.db.session.commit()
        self.id_ctr += 1

    def sell(self, symbol, shares):

        logging.info("SELL ORDER RECIEVED!!!")
        date = datetime.now()
        order = Order(self.id_ctr, symbol, shares)
        self.db.session.add(order)
        self.db.session.commit()
        self.id_ctr += 1

    def get_orders(self, amount=10):
        orders = self.db.execute(select(Order).order_by("id", reversed).limit(
            amount))
        return orders