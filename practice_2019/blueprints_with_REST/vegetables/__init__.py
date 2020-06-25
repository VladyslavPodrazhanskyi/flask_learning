from flask import Blueprint
from flask_restful import Api
from vegetables.vegetables import Vegetables

vegetables_bp = Blueprint("vegetables", __name__)

api = Api(vegetables_bp)



api.add_resource(Vegetables, "/vegetables", '/vegetables/<string:value>')