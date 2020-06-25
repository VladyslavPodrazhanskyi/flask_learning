from flask_restful import Resource

class Fish(Resource):
    def get(self):
        return "This page was not found", 404