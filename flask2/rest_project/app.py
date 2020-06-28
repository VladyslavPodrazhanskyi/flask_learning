from flask import Flask, request
from flask_restful import Api, Resource, reqparse
app = Flask(__name__)

api = Api(app)

parser_core = reqparse.RequestParser(bundle_errors=True)
parser_core.add_argument('page', required=True, type=int)  # help="message" help="incorrect type of page"
parser_core.add_argument('name', type=str, action='append') # without action='append'
#  - переменной name- присваивается только первое значение аргумента.
# http://127.0.0.1:5000?page=34&page=45&page=20&name=Igor&name=Nick
# {'page': 34, 'name': ['Igor', 'Nick']}
parser_core.add_argument('from-header', required=True, type=int, location='headers')
parser_core.add_argument('cookiesargs', required=True, type=int, location='cookies')
parser_core.add_argument('bodyarg', type=int, location='form')

# Home

class CoreResource(Resource):
    def get(self):
        args = parser_core.parse_args(strict=True) # restricts other arguments ( not included in parser).
        print(args)
        return {'key1': 'value1'}, 200, {'customs_header': 'header_value'}

    def post(self):
        args = parser_core.parse_args(strict=True)
        print(args)
        return 'post'

# company restful service

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
