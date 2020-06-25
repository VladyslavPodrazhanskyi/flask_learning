from flask import Blueprint, request, redirect, url_for
from practice_2019.flask_training import do_get, do_post, do_delete

fruites_bp = Blueprint('fruites_bp', __name__, template_folder='templates')

fruites_list = ['apple', 'pair', 'plum']

@fruites_bp.route('/fruites')
@fruites_bp.route('/fruites/<string:value>', methods=['GET', 'POST', 'DELETE'])
def fruites_page(value=None):
    if request.method == 'POST':
        return do_post(value, fruites_list)
    elif request.method == 'DELETE':
        return do_delete(value, fruites_list)
    return do_get('fruites.html', fruites_list)


@fruites_bp.route('/fruit')
@fruites_bp.route('/fruite')
def fruites_redirect():
    return redirect(url_for('fruites_bp.fruites_page'))