from flask import Blueprint, request
from method_functions import do_post, do_get, do_delete

vegetables = Blueprint("vegetable_fjskj", __name__, template_folder="vegetables_templates")

vegetables_db = ["potato", "cucumber", "carrot", "tomatto"]



@vegetables.route("/vegetables")
@vegetables.route("/vegetables/<string:value>", methods=['GET', 'POST', 'DELETE'])
def vegetables_mthods(value=None):
    if request.method == "POST":
        return do_post(vegetables_db, value)
    elif request.method == "DELETE":
        return do_delete(vegetables_db, value)
    else:
        return do_get("vegetables.html", vegetables_db)

