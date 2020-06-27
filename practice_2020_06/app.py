import os
import json
from pprint import pprint
from flask import (Flask, request, url_for,
    render_template, jsonify, redirect,
    abort,session, make_response)

from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config['SECRET_KEY'] = b'\x9e|\x95\xe7\xa3O\xba\x12\x16 \x1d\x96\xd6\x0f\xfcv)\xe5mi\xe4\xd8\xe4L'
# app.secret_key =  ...


@app.route('/')
def index():
    pprint(dir(app))
    # print(dir(request))     # request.__dict__  http://jsonviewer.stack.hu/
    return '<h1>This is index page</h1>'

# 2 decorators:
@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    if name:
        return f'Hello, {name}!'
    return 'Hello, stranger!'


# different types of vars:

@app.route('/string/<val>')
def check_string(val):
    if isinstance(val, str):
        return f"I'm string values {val}"


@app.route('/int/<int:val>')
def check_int(val):
    if isinstance(val, int):
        return f'I am int value {val}'


@app.route('/float/<float:val>')
def check_float(val):
    if isinstance(val, float):
        return f'I am float value {val}'


@app.route('/uuid/<uuid:val>')
def check_uuid(val):
    type_val = str(type(val))
    return f"I'm UUID value {val}, type {type_val}"




# home and about

@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def about_page():
    return render_template('about.html')


# Object request:

@app.route('/request')
def get_request():
    client_name = request.headers.get('client_name')
    browser = request.headers.get('User-Agent')
    cookies = request.cookies

    args = request.args
    base_url = request.base_url
    method = request.method

    response = dict()
    response['client_name'] = client_name
    response['args'] = args
    response['base_url'] = base_url
    response['browser'] = browser
    response['cookies'] = cookies
    response['method'] = method

    return jsonify(response)






# cookies (consol/ application in browser):
@app.route('/get_cookies')
def get_cookies():
    cookies = request.cookies
    return jsonify(cookies)



@app.route('/set_cookies', methods=['POST'])
def set_cookies():
    response = make_response("cookies added successfully")
    for key, value in json.loads(request.data).items():
        response.set_cookie(key, value)
    return response

# set cookie with get to browser:
# без сессии данные не зашифрованы.
@app.route('/cookie_to_browser')
def cookie_to_browser():
    response = make_response('cookie added')
    response.set_cookie("key1", 'val1')
    return response

# use session:

@app.route('/test_session')
def test_session():
    session['sessin_key'] = 'session_value'
    session['name'] = request.args.get('name')
    return "session key and value added"

#logging  - документирвоание ошибок.
# https://docs.python.org/3/library/logging.html

@app.route('/logging')
def logging():
    app.logger.debug('debug value')  # appear in consol if debug=True only!
    app.logger.warning('warning value')
    app.logger.error('error value')
    return 'Test loging'



#bluepring
from messenger import messenger_bp
app.register_blueprint(messenger_bp)



# work with files:

# read from files  - path from url:
@app.route('/read_from_file/<path:val>')  # files/file_for_read.txt
def get_data_from_file(val):
    with open(val) as f:
        return f.read()



#file uploads

@app.route('/upload', methods=['POST'])
def file_upload():
    file = request.files['file']
    file_path = os.path.join('files', secure_filename(file.filename))
    file.save(file_path)

    with open(file_path) as f:
        return f.read()


# upload file from form

from flask_wtf import FlaskForm
from wtforms import SubmitField, FileField

class UploadFileForm(FlaskForm):
    file_field = FileField('Upload File')
    submit = SubmitField('Upload')

@app.route('/file_from_form', methods=['POST', 'GET'])
def form_upload():
    session['content'] = None
    form = UploadFileForm()
    if form.validate_on_submit():
        file = request.files[form.file_field.name]
        file_path = os.path.join('files', secure_filename(file.filename))
        file.save(file_path)
        with open(file_path) as f:
            content = f.read()
            print(type(content))
            session['content'] = content
        return redirect(url_for('read_content', content=content))
    return render_template('upload_file.html', form=form)


@app.route('/content')
def read_content():
    content = 'empty'
    if session.get('content'):
        content = session.get('content')
    return content


# errors and errorhandlers:

@app.route('/error_404')
def error_404():
    abort(404, 'page is not found')


@app.errorhandler(404)
def page_not_found(error):
    return render_template("error_404.html", error=error), 404



if __name__ == "__main__":
    app.run(debug=True)