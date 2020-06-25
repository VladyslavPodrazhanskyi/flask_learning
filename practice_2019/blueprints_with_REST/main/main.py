from flask_restful import Api, Resource


class Main(Resource):
    def get(self):
        return 'This is main page, choose vegetables, or fruites'
    
    
    