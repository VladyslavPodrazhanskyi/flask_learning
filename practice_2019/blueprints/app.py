from flask import Flask, request, render_template, redirect, url_for, abort
from fruites.fruites_routes import fruites
from vegetables.vegetables_routes import vegetables
app = Flask(__name__)




@app.route('/')
def main():
    return '<h1>This is main page, choose vegetables, or fruites</h1>'


@app.route("/meat")
def meat():
    return redirect(url_for("main"))

@app.route("/fish")
def fish():
    abort(404)

@app.errorhandler(404)
def error_404(error):
    return "Sorry but this page is not found"




app.register_blueprint(fruites)
app.register_blueprint(vegetables)

if __name__ == '__main__':
    app.run(debug=True)


