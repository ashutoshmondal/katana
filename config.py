##OPEN API STUFF
OPENAI_API_KEY = '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'



## FLASK STUFF
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "this-is-a-super-secret-key"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
