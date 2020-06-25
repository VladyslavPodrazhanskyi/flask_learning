from flask import render_template

def do_post(data, value):
    data.append(value)
    return "successfully added"

def do_delete(data, value):
    if value in data:
        data.remove(value)
        return "successfully deleted"
    else:
        return "current value is absent"

def do_get(template_file, data):
    return render_template(template_file, data=data)