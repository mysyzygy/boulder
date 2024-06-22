

from app import db
import json

class Ticker(db.Model):
    __tablename__ = 'tickers'
    symbol_date_id = db.Column(db.Text, primary_key=True)
    symbol = db.Column(db.Text, nullable=False)
    date = db.Column(db.Text, nullable=False)
    open = db.Column(db.Float, nullable=False)
    high = db.Column(db.Float, nullable=False)
    low = db.Column(db.Float, nullable=False)
    close = db.Column(db.Float, nullable=False)
    volume = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return (f'{self.symbol_date_id}: Symbol, {self.symbol}, Date:'
                f' {self.date}, Open: {self.open},'
                f'High {self.high}, Low: {self.low}, Close {self.close},'
                f'Volume: {self.volume}')

    def to_dict(self):
        return {"symbol_date_id": self.symbol_date_id,
                "symbol": self.symbol,
                "date": self.date,
                "open": self.open,
                "high": self.high,
                "low": self.low,
                "close": self.close,
                "volume": self.volume
                }
    def to_json(self):
        return json.dumps(self.to_dict())
