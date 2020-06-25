from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>This is home page</h1>'

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


@app.route('/read_from_file/<path:val>')  # http://127.0.0.1:5000/read_from_file/files/file_for_read.txt
def get_data_from_file(val):
    with open(val) as f:
        data = f.read()
        return data

@app.route('/uuid/<uuid:val>')
def check_uuid(val):
    type_val = str(type(val))
    return f"I'm UUID value {val}, type {type_val}"

'2ed29aeb-023d-444b-a576-3d1370a7aa11'


@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    if name:
        return f'Hello, {name}!'
    return 'Hello, stranger!'


if __name__ == "__main__":
    app.run(debug=True)