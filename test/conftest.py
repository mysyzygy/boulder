import os
import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import URL, create_engine
from sqlalchemy.orm import sessionmaker


class TestConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'  # Using SQLite for testing
    SQLALCHEMY_TRACK_MODIFICATIONS = False

db = SQLAlchemy()


@pytest.fixture(scope='module')
def fake_app():
    app = Flask(__name__)
    app.config.from_object(TestConfig)
    db.init_app(app)
    testing_client = app.test_client()
    ctx = app.app_context()
    ctx.push()
    yield testing_client, db
    ctx.pop()

