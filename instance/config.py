class Config():
    DEBUG=False
    DB_NAME = 'RMC'
class DevelopmentConfig(Config):
    """
    Enable our debug mode to True
    in development in order to auto
    restart our server on code changes
    """
    DEBUG = True
    DB_URI = 'mongodb://localhost:27017/' # Different environments to use different db instance
app_configuration={
    'development': DevelopmentConfig
}

AppConfig = app_configuration.get('development')

