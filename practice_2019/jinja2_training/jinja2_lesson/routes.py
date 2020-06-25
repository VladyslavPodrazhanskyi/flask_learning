from flask import Blueprint, render_template

lesson = Blueprint('lesson', __name__, template_folder='templates')


@lesson.route('/lesson')
def template_test():
    return render_template('child.html', my_string='Whee!', my_list=[0, 1, 2, 3, 4, 5], title='CHILD')

@lesson.route('/lesson/parent')
def parent_test():
    return render_template('parent.html', my_string='Whee!', my_list=[0, 1, 2, 3, 4, 5], title='PARENT')

@lesson.route('/lesson1')
def lesson1():
    return render_template('lesson1.html')

@lesson.route('/lesson2')
def lesson2():
    return render_template('lesson2.html')

@lesson.route('/lesson3')
def lesson3():
    return render_template('lesson3.html')