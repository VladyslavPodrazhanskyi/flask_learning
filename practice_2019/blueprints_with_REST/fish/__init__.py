from flask import Blueprint
from flask_restful import Api
from fish.fish import Fish

fish_bp = Blueprint("fish", __name__)

api = Api(fish_bp)


api.add_resource(Fish, "/fish")