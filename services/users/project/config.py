# Configures which stage of the project to run

class BaseConfig:
    '''Base configuration'''
    TESTING = False

class DevelopmentConfig:
    '''Development configuration'''
    pass

class TestingConfig:
    '''Testing configuration'''
    TESTING = True

class ProductionConfig:
    '''Production configuration'''
    pass
