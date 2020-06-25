from flask import Blueprint, request, jsonify, make_response

cookies_bp = Blueprint('cookies_bp', __name__)

@cookies_bp.route('/get_cookies')
def get_cookies():
    return jsonify(request.cookies)

cookies_from_server = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value3',
}

@cookies_bp.route('/set_cookies')
def set_cookies():
    response = make_response('cokies successfully added from the server')
    for k, v in cookies_from_server.items():
        response.set_cookie(k, v)
    return response


@cookies_bp.route('/cookies_from_ui_body', methods=["POST"])
def set_cookies_from_iu():
    import json
    response = make_response('cookies successfull added from ui body')
    for k, v in json.loads(request.data).items():
        print(k, v)
        response.set_cookie(k, v)
    return response








