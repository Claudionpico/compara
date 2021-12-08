import os

class Config:
    GENERAL = {
        'host': os.environ['HOST'],
        'port': os.environ['PORT'],
        'threaded': 0,
        'username':os.environ['USERNAME'],
        'password':os.environ['PASSWORD'],
        'databases': {
            'pool_recycle': 1200,
            'mysql': 'mysql://'+os.environ['DB_USER']+':'+os.environ['DB_PASS']+'@'+os.environ['DB_HOST']+'/'+os.environ['DB_NAME']
        }
    }

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
'development': DevelopmentConfig,
'production': ProductionConfig,
'default': DevelopmentConfig
}
