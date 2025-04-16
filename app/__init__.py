# app/__init__.py
from flask import Flask
from models.base import db
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    Migrate(app, db)

    # Import models here so they are registered
    from models.article import Article
    from models.source import Source

    @app.route("/")
    def home():
        return "RSS Summarizer is running"

    return app
