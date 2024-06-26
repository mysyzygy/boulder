from flask import render_template, request
from .models import Ticker, Order


def register_routes(app, db):
    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'GET':
            tickers = db.session.query(Ticker).order_by(Ticker.date.desc()).limit(
            10).all()
            orders = db.session.query(Order).order_by(
                Order.date.desc()).limit(
                10).all()
            return render_template("index.html",
                                   tickers=tickers,
                                   orders=orders)
        elif request.method == 'POST':
            symbol_date_id = request.form['symbol_date_id']
            symbol = request.form['symbol']
            date = request.form['date']
            open = request.form['open']
            high = request.form['high']
            low = request.form['low']
            close = request.form['close']
            volume = request.form['volume']

            ticker = Ticker(
                symbol_date_id=symbol_date_id,
                symbol=symbol,
                date=date,
                open=open,
                high=high,
                low=low,
                close=close,
                volume=volume,
            )

            db.session.add(ticker)
            db.session.commit()
            tickers = Ticker.query.all()
            return render_template("index.html", tickers=tickers)

    # @app.route('/delete/<pid>', methods=["DELETE"])
    # def delete(pid):
    #     Person.query.filter(Person.pid == pid).delete()
    #     db.session.commit()
    #     people = Person.query.all()
    #     return render_template("index.html", people=people)
    #
    # @app.route('/detail/<pid>')
    # def detail(pid):
    #     person = Person.query.filter(Person.pid == pid).first()
    #     return render_template('detail.html', person=person)