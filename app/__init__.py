"""Application factory ของเว็บแอปพลิเคชันแนะนำแล็ปท็อป"""
from pathlib import Path

from flask import Flask

from .config import Config
from .extensions import db

BASE_DIR = Path(__file__).resolve().parent.parent


def create_app(config_class=Config):
    app = Flask(
        __name__,
        template_folder=str(BASE_DIR / "templates"),
        static_folder=str(BASE_DIR / "static"),
        static_url_path="/static",
    )
    app.config.from_object(config_class)

    db.init_app(app)

    from .routes.main import main_bp
    from .routes.catalog import catalog_bp
    from .routes.recommendation import recommendation_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(catalog_bp)
    app.register_blueprint(recommendation_bp)

    from .errors import register_error_handlers

    register_error_handlers(app)

    return app
