from flask import Blueprint, request
from practice_2019.flask_training import do_get, do_post, do_delete

vegetables_bp = Blueprint('vegetables_bp', __name__, template_folder='templates')


vegetables_list = ['potato', 'cucumber', 'garlic']


@vegetables_bp.route('/vegetables')
@vegetables_bp.route('/vegetables/<string:value>', methods=['GET', 'POST', 'DELETE'])
def vegetables(value=None):
    if request.method == 'POST':
        return do_post(value, vegetables_list)
    elif request.method == 'DELETE':
        return do_delete(value, vegetables_list)
    return do_get('vegetables.html', vegetables_list)



