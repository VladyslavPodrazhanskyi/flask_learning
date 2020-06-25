from flask import Flask, request, render_template, redirect, url_for, abort

app = Flask(__name__)

vegetables = ["potato", "cucumber", "carrot", "tomatto"]
fruites = ["apricot", "cherry", "grapes", "apple"]

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

@app.route('/')
def main():
    return '<h1>This is main page, choose vegetables, or fruites</h1>'

@app.route("/vegetables")
@app.route("/vegetables/<string:value>", methods=['GET', 'POST', 'DELETE'])
def vegetables_mthods(value=None):
    if request.method == "POST":
        return do_post(vegetables, value)
    elif request.method == "DELETE":
        return do_delete(vegetables, value)
    else:
        return do_get("vegetables.html", vegetables)


@app.route("/fruites")
@app.route("/fruites/<string:value>", methods=["GET", "POST", "DELETE"])
def fruites_methods(value=None):
    if request.method == "POST":
        return do_post(fruites, value)
    elif request.method == "DELETE":
        return do_delete(fruites, value)
    else:
        return do_get("fruites.html", fruites)


@app.route("/meat")
def meat():
    return redirect(url_for("main"))

@app.route("/fish")
def fish():
    abort(404)

@app.errorhandler(404)
def error_404(error):
    return "Sorry but this page is not found"


if __name__ == '__main__':
    app.run()
