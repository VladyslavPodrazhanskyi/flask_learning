from typing import List

from flask import Flask, abort, redirect, url_for
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

vegetables = ["potato", "cucumber", "carrot", "tomatto"]

fruites = ["apricot", "cherry", "grapes", "apple"]


class Main(Resource):
    def get(self):
        return 'This is main page, choose vegetables, or fruites'


# def do_post(data, value):
#     data.append(value)
#     return "successfully added"
#
# def do_delete(data, value):
#     if value in data:
#         data.remove(value)
#         return "successfully deleted"
#     else:
#         return "current value is absent"
#
# def do_get(template_file, data):
#     return render_template(template_file, data=data)

class Vegetables(Resource):
    def get(self, value=None):
        response = dict()
        for i, element in enumerate(vegetables):
            response[i + 1] = element
        return response

    def post(self, value):
        vegetables.append(value)
        return "Value is added successfully"

    def delete(self, value):
        if value in vegetables:
            vegetables.remove(value)
            return "value is deleted successfully"
        return "the value is absent"


class Fruites(Resource):

    def get(self, value=None):
        response = dict()
        for i, element in enumerate(fruites):
            response[i + 1] = element
        return response

    def post(self, value):
        fruites.append(value)
        print(fruites)
        return "Value is added successfully"

    def delete(self, value):
        if value in fruites:
            fruites.remove(value)
            return "value is deleted successfully"
        return "the value is absent"


class Fish(Resource):
    def get(self):
        abort(404)


class Error404(Exception):
    def __init__(self):
        self.code = 404
        self.message = "Sorry but this page is not found"


#     @app.errorhandler(404)
#     def error_404(error):
#         return "Sorry but this page is not found"
# #
# @app.route("/meat")
# def meat():
#     return redirect(url_for("main"))
#
# @app.route("/fish")


api.add_resource(Main, "/", "/meat")
api.add_resource(Vegetables, "/vegetables", '/vegetables/<string:value>')
api.add_resource(Fruites, "/fruites", "/fruites/<value>")
api.add_resource(Fish, "/fish")

if __name__ == '__main__':
    app.run()
