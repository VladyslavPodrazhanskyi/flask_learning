from flask import render_template

def do_get(template, list):
    return render_template(template, list=list)

def do_post(value, list):
    if value not in list:
        list.append(value)
        return 'successfully added'
    return 'current item is on the list already'

def do_delete(value, list):
    if value in list:
        list.remove(value)
        return 'the item successfully delete'
    return 'This is item is not available in the list'