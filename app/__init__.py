# !/usr/bin/env python3
import requests
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import migrate, Migrate

from datetime import datetime
import os
from config import Config

from datetime import datetime

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    # create and configure the app
    app = Flask(__name__, template_folder='templates')
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import register_routes
    register_routes(app, db)

    return app

