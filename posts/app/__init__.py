from flask import Flask
from .model import db
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    # Регистрация Blueprints
    from .route import posts_bp

    app.register_blueprint(posts_bp, url_prefix='/posts')

    return app
