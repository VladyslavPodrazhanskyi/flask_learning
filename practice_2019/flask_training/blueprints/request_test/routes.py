from flask import Blueprint, request, jsonify, render_template


request_bp = Blueprint('request_bp', __name__, template_folder='templates')


@request_bp.route('/request', methods=["GET", "POST"])
def request_view():
    args = request.args
    base_url = request.base_url
    name = request.headers.get('name')
    date = request.headers.get('date')

    response = dict()
    response['args'] = args
    response['base_url'] = base_url
    response['name'] = name
    response['date'] = date
    return jsonify(response)


@request_bp.route('/browser')
def browser():
    user_agent = request.headers.get('User-Agent')
    return render_template('browser.html', browser=user_agent)


@request_bp.route('/headers')
def get_headers():
    headers_dict = request.headers.items()
    return render_template('headers.html', headers_dict=headers_dict)

