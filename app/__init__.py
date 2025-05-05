from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    from .config import Config
    app.config.from_object(Config)

    db.init_app(app)

    from .routes import chores_bp
    app.register_blueprint(chores_bp)

    return app
