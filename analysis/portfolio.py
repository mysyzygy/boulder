from datetime import datetime
from app import db
from app.models import Order
from sqlalchemy import select


class Portfolio:
    def __init__(self, socketio, cash):
        self.cash = cash
        self.db = db
        self.id_ctr = 0
        socketio.on_event('buy_event', self.buy)
        socketio.on_event('sell_event', self.sell)

    def buy(self, data):
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
        date = datetime.now()
        order = Order(self.id_ctr, symbol, shares)
        self.db.session.add(order)
        self.db.session.commit()
        self.id_ctr += 1

    def get_orders(self, amount=10):
        orders = self.db.execute(select(Order).order_by("id", reversed).limit(
            amount))
        return orders