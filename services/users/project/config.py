# Configures which stage of the project to run

import os

class BaseConfig:
    '''Base configuration'''
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig:
    '''Development configuration'''
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

class TestingConfig:
    '''Testing configuration'''
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL')

class ProductionConfig:
    '''Production configuration'''
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
