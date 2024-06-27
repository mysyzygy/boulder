from app.models import Ticker, Order

#
# def test_add_retrieve_data(fake_app):
#     testing_client, db= fake_app
#
#     test_data = Ticker(symbol_date_id="123",
#                 symbol= "AAPL",
#                 date= "01-01-2024",
#                 open= 1,
#                 high= 2,
#                 low= 0,
#                 close=1,
#                 volume= 100
#                )
#     db.session.add(test_data)
#     db.session.commit()
#
#     result =  db.session.query(Ticker).all()
#     assert len(result) == 1
#     assert result[0].symbol == "AAPL"
#     assert result[0].volume == 100
#
