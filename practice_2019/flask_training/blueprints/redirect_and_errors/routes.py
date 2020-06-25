from flask import Blueprint, render_template, url_for, redirect, abort

redirect_and_errors_bp = Blueprint('redirect_and_errors_bp', __name__, template_folder='templates')

@redirect_and_errors_bp.route('/redirect_main')
def redirect_main():
    return redirect(url_for('valueables.home'))

@redirect_and_errors_bp.route('/redirect')
@redirect_and_errors_bp.route('/redirect/<value>')
def redirect_universal(value=None):
    if value == 'about':
        return redirect(url_for('valueables.about'))
    elif value == 'html':
        return redirect(url_for('html_test.html_test_1'))
    return redirect(url_for('valueables.home'))

@redirect_and_errors_bp.route('/abort/<int:code>')
def test_abort(code):
    abort(code)


@redirect_and_errors_bp.route('/abort_with_message/<int:value>')
def abort_with_message(value):
    abort(value, f'We have error with code {value}')