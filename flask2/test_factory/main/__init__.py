# main/__init__.py
# http://jsonviewer.stack.hu/
import os
from pprint import pprint
from flask import Blueprint, current_app

main = Blueprint('main', __name__)


@main.route('/')
def hell_from_main():
    print(os.environ.get('ENV'))
    print(current_app.config)
    return current_app.config.get('DB_CONNECTION')



