from flask import Blueprint, render_template
from flask_login import login_required

bp = Blueprint("orders", __name__)

@bp.route("/")
@login_required
def index():
    # return "Order Up!"
    return render_template("orders.html")
