from flask import Blueprint
from flask_restful import Api
from fruites.fruites import Fruites

fruites_bp = Blueprint("fruites", __name__)


api = Api(fruites_bp)



api.add_resource(Fruites, "/fruites", "/fruites/<value>")







