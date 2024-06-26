**Trading App**

Currently, pulls bitcoin data from polygon.io. price_event updates UI with 
realtime data. Simultaneously, the data is stored in a database, which 
updates in the web app on browser refresh. 

App is currently hosted here:

https://djone-ba5640b7e107.herokuapp.com/

**Setup Data Credentials** 

Goto https://polygon.io/ create an account and subscribe to currency data 
starter account.

Create a POLYGON_API_KEY environment variable.

**Install Requirements**

$ pip install -e . -r requirements.txt

**Setup Database**

$ flask db init
$ flask db migrate -m "new migration"
$ flask db upgrade

**Running**

To run with python 

$ python run.py

To with gunicorn

$ gunicorn -b 0.0.0.0:8000 --worker-class eventlet -w 1 run:app


