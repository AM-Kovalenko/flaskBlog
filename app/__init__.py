import os
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_object=None):
    app = Flask(__name__, instance_relative_config=False)
    if config_object is None:
        # конфиг берётся из env или default
        from .config import Config
        app.config.from_object(Config)
    else:
        app.config.from_object(config_object)

    # init extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # регистрируем blueprint
    from .routes import bp as main_bp
    app.register_blueprint(main_bp)

    return app
