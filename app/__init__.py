from flask import Flask
from config import config

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # route blueprint
    from .main import main_BP
    from .make_fake import make_fake_BP
    app.register_blueprint(main_BP)
    app.register_blueprint(make_fake_BP, url_prefix='/make_fake')

    return app

