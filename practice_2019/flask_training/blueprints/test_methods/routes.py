from flask import Blueprint, render_template, request

test_methods_bp = Blueprint('test_methods', __name__, template_folder='method_templates')


test_methods_list = ['value1', 'value2', 'value3']   #мнимая база данных


@test_methods_bp.route('/test_methods')
@test_methods_bp.route("/test_methods/<value>", methods=['GET', 'POST', 'DELETE'])
def test_methods_func(value=None):
    if request.method == 'POST':
        return do_post(value)
    elif request.method == 'DELETE':
        return do_delete(value)
    return do_get()

def do_get():
    return render_template('test_methods.html', test_methods_list=test_methods_list)

def do_post(new_value):
    test_methods_list.append(new_value)
    return 'successfully added new value'

def do_delete(value):
    if value in test_methods_list:
        test_methods_list.remove(value)
        return 'successfully deleted'
    else:
        return 'current value is absent'