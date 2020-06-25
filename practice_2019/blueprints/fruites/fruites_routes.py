from flask import Blueprint, request
from method_functions import do_get, do_delete, do_post


fruites = Blueprint("fruites", __name__, template_folder="fruites_templates")

fruites_db = ["apricot", "cherry", "grapes", "apple"]



@fruites.route("/fruites")
@fruites.route("/fruites/<string:value>", methods=["GET", "POST", "DELETE"])
def fruites_methods(value=None):
    if request.method == "POST":
        return do_post(fruites_db, value)
    elif request.method == "DELETE":
        return do_delete(fruites_db, value)
    else:
        return do_get("fruites.html", fruites_db)