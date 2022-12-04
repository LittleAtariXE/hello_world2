import os

basedir = os.path.dirname(os.path.abspath(__file__))

class Config:
    SECRET_KEY = 'supersecretkey'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    pass

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}