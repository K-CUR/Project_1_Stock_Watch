from flask import Flask, render_template, url_for
from flask import Blueprint

from models.fabric import Fabric
from models.manufacturer import Manufacturer

import repositories.fabric_repository as fabric_repository
import repositories.manufacturer_repository as manufacturer_repository


fabrics_blueprint = Blueprint("fabrics", __name__)
manufacturers_blueprint = Blueprint("manufacturers", __name__)


@fabrics_blueprint.route("/fabrics")
def fabrics():
    fabrics = fabric_repository.select_all()
    return render_template("/fabrics/index.html", fabrics = fabrics)


@manufacturers_blueprint.route("/manufacturer/<id>")
def show_manufacturer(id):
    manufacturer = manufacturer_repository.select(id)
    return render_template("/manufacturer/show.html", manufacturer = manufacturer)

