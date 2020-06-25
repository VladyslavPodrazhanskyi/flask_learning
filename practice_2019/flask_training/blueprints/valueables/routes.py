from flask import render_template, Blueprint


valueables = Blueprint('valueables', __name__, template_folder='template')


@valueables.route("/")
def home():
    return render_template('home.html')


@valueables.route('/about')
def about():
    return render_template('about.html')


@valueables.route('/name/<int:index>')
def name(index):
    name_list = ['Inna', 'Lena', 'Serge']
    try:
        return f'You choose name {name_list[index]}'
    except IndexError:
        return 'You are out of range'


@valueables.route('/float/<float:num>')
def float_test(num):
    if isinstance(num, float):
        return f'You input Number: {num*2}'
    else:
        return 'input argument in float format'


@valueables.route('/string/<arg>')
def string_test(arg):
    if isinstance(arg, str):
        return f"{arg} - Yes, this is string"

@valueables.route('/path/<path:value>')
def path_test(value):
    return value

