# !/usr/bin/env python3
import requests
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import migrate, Migrate
from datetime import datetime
import os

from datetime import datetime

db = SQLAlchemy()

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, template_folder='templates')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./testdb.db'

    db.init_app(app)

    from routes import register_routes
    register_routes(app, db)

    migrate = Migrate(app, db)

    return app


