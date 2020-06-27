# config.py
# to change config export ENV=DEV or TEST
import os


class Config():
    DEFAULT = "default_val"
    DB_CONNECTION = 'default_connection'


class TestConfig(Config):
    DB_CONNECTION = 'test_connection'


class DevConfig(Config):
    DB_CONNECTION = 'dev_connection'


def run_config():
    env = os.environ.get('ENV')
    if env == "TEST":
        return TestConfig
    elif env == "DEV":
        return DevConfig
    else:
        return Config


