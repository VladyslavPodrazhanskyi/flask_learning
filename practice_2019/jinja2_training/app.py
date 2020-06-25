import datetime
from flask import Flask, render_template, request
from random import randint
# from flask_script import Manager

app = Flask(__name__)


# manager = Manager(app)

# Create customs filter with decorator @app.template_filter
@app.template_filter('my_filter')  # we can put name of filter as agrument in decorator
def datetimefilter(value, format='%Y/%m/%d %H:%M'):
    """"convert a datetime to a different format."""
    return value.strftime(format)  # strftime - convert class date to string


# Add the filter to Jinja environment
app.jinja_env.filters['my_filter'] = datetimefilter


# Customs filter - return sum of elements of the list
@app.template_filter()
def sum_list_filter(value: list):
    return sum(value)


app.jinja_env.filters['sum_list_filter'] = sum_list_filter


@app.route('/')
def home():
    gen_list = [n for n in range(randint(5, 100))]
    return render_template('index.html', current_time=datetime.datetime.now(), value=gen_list)


@app.route('/user/')
@app.route('/user/<name>')
def user(name='Stranger'):
    age = request.args.get('age')
    if age:
        age = float(age)
    return render_template('user.html', name=name, age=age)


# <p>A value from a dictionary {{ my_dict['key1'] }}</p>
# <p>A value from a list {{ my_list[4] }}</p>
# <p>A value from a list with var index {{ my_list[var] }}</p>
# <p>A value from a object's method {{ my_cat.distance() }}</p>

my_dict = {'key1': 1234, 'key2': 1111}
my_list = [0, 1, 2, 3, 4, 5, ]


class Cat():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.speed = 5
        self.walk_time = 1

    def distance(self):
        return self.speed * self.walk_time


my_cat = Cat('Barsic', 15)
my_string = '<h1>This is my string</h1>'


@app.route('/var/<int:var>')
def get_var(var):
    return render_template('var_types.html', my_string=my_string, my_dict=my_dict, my_list=my_list, var=var,
                           my_object=my_cat)


@app.route('/macros_inside')
def macros_inside():
    massive = my_list
    return render_template('html_with_macros_inside.html', massive=massive)


@app.route('/import_macros')
def import_macros():
    massive = my_dict.items()
    return render_template('import_macros.html', massive=massive)


@app.route('/from_base')
def from_base():
    return render_template('from_base.html')


from .jinja2_lesson.routes import lesson

app.register_blueprint(lesson)

if __name__ == "__main__":
    app.run(debug=True)  # flask run ( дебаг не работает), но работают блупринтын;
    # python app.py - дебаг работает, но не работают блупринты
    # export FLASK_ENV=development - позволяет использовать для запуска flask run в режиме дебага.
