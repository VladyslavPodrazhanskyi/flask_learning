# messenger/__init__.py

from flask import Blueprint, render_template


messenger_bp = Blueprint('messenger_bp', __name__, template_folder='templates')


@messenger_bp.route('/messenger')
def messenger():
    return render_template('mess.html')