"""
Config file contains global CONSTANTS
"""
import os


class Config:
    """Parent settings file"""

    DEBUG = True
    


class DevelopmentConfig(Config):
    """Development configuration"""

    DEBUG = True


class TestingConfig(Config):
    """Configurations for Testing"""

    Testing = True
    DEBUG = True


class StagingConfig(Config):
    """Configurations for staging"""

    DEBUG = False


class ProductionConfig(Config):
    """Configurations for Production."""

    DEBUG = False
    TESTING = False


APP_CONFIG = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}