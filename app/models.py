

from app import db


class Ticker(db.Model):
    __tablename__ = 'tickers'

    name = db.Column(db.Text, primary_key=True)
    date = db.Column(db.Text, nullable=False)
    open = db.Column(db.Float, nullable=False)
    high = db.Column(db.Float, nullable=False)
    low = db.Column(db.Float, nullable=False)
    close = db.Column(db.Float, nullable=False)
    volume = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return (f'Name: {self.name}, Date: {self.date}, Open: {self.open},'
                f'High {self.high}, Low: {self.low}, Close {self.close},'
                f'Volume: {self.volume}')
