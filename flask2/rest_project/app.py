from flask import Flask, request
from flask_restful import Api, Resource
app = Flask(__name__)

api = Api(app)

class CoreResource(Resource):
    def get(self):
        return {'key1': 'value1'}, 301, {'customs_header': 'header_value'}

    def post(self):
        return 'post'


companies = ['Amazon', 'Apple', 'Microsoft']

class Companies(Resource):
    def get(self):
        response = dict()
        for i, el in enumerate(companies):
            response[i + 1] = el
        return response

    def post(self, value):
        companies.append(value)
        return {'result': 'added successfully'}

    def put(self):
        import json
        update_dict = json.loads(request.data)
        company = update_dict.get('company')
        position = update_dict.get('position') - 1
        companies.remove(company)
        companies.insert(position, company)
        return {'result': 'updated_successfully'}

    def delete(self, value):
        if value in companies:
            companies.remove(value)
            return {'result': 'deleted successfully'}
        return {'result': 'value is absent'}




api.add_resource(CoreResource, '/')
api.add_resource(Companies, '/companies', '/companies/<value>')

if __name__ == '__main__':
    app.run(debug=True)
