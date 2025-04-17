from flask import Flask
from models.base import db
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

def create_app():
    load_dotenv()

    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    Migrate(app, db)

    # Import models to register them with SQLAlchemy
    from models.article import Article
    from models.source import Source

    # Register blueprints
    from routers.articles import bp as articles_bp
    app.register_blueprint(articles_bp)
    
    from routers.sources import bp as sources_bp
    app.register_blueprint(sources_bp)

    @app.route("/")
    def home():
        return "RSS Summarizer is running"

    return app
