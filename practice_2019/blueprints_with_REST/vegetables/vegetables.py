from flask_restful import Resource
from vegetables.vegetables_db import vegetables_db

class Vegetables(Resource):
    def get(self, value=None):
        response = dict()
        for i, element in enumerate(vegetables_db):
            response[i + 1] = element
        return response

    def post(self, value):
        vegetables_db.append(value)
        return "Value is added successfully"

    def delete(self, value):
        if value in vegetables_db:
            vegetables_db.remove(value)
            return "value is deleted successfully"
        return "the value is absent"