from flask import Blueprint, render_template

main_hw1_bp = Blueprint('main_hw1_bp', __name__, template_folder='templates')


@main_hw1_bp.route('/main_hw1')
def main_hw1():
    return render_template('main_hw1.html')
