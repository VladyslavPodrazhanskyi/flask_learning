from flask_restful import Resource
from fruites.fruites_db import fruites_db

class Fruites(Resource):

    def get(self, value=None):
        response = dict()
        for i, element in enumerate(fruites_db):
            response[i + 1] = element
        return response

    def post(self, value):
        fruites_db.append(value)
        return "Value is added successfully"

    def delete(self, value):
        if value in fruites_db:
            fruites_db.remove(value)
            return "value is deleted successfully"
        return "the value is absent"
