from flask import Blueprint, render_template

html_test = Blueprint('html_test', __name__, template_folder='templates')


@html_test.route('/html1')
def html_test_1():
    return render_template('html_basic.html')