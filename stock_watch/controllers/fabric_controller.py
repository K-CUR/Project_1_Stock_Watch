from flask import Flask, render_template, url_for, request, redirect
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
    manufacturers = manufacturer_repository.select_all()
    return render_template("/fabrics/index.html", fabrics = fabrics, all_manufacturers = manufacturers)


@fabrics_blueprint.route("/fabrics/new", methods =['GET'])
def new_fabric():
    manufacturers = manufacturer_repository.select_active()
    colours = ["Green", "Blue", "Pink", "Red", "White", "Yellow", "Purple", "Teal", "Multi-coloured", "Brown", "Grey", "Orange", "Black"]
    styles = ["Plain", "Stripe", "Check", "Polka dot", "Chevron", "Geometric", "Floral", "Illustration"]
    return render_template("/fabrics/new.html", all_fabrics = fabrics, all_manufacturers = manufacturers, all_colours = colours, all_styles = styles)



@fabrics_blueprint.route("/fabrics", methods=['POST'])
def create_fabric():
    manufacturer_id = request.form['manufacturer_id']
    design_ref = request.form['design_ref']
    main_colour = request.form['main_colour']
    style = request.form['style']
    stock_price = request.form['stock_price']
    sale_price = request.form['sale_price']
    quantity = request.form['quantity']
    manufacturer = manufacturer_repository.select(manufacturer_id)
    fabric = Fabric(manufacturer, design_ref, main_colour, style, stock_price, sale_price, quantity)
    fabric_repository.save(fabric)
    return redirect("/fabrics")


@fabrics_blueprint.route("/fabrics/<id>/edit", methods=['GET'])
def edit_fabric(id):
    fabric = fabric_repository.select(id)
    manufacturers = manufacturer_repository.select_all()
    colours = ["Green", "Blue", "Pink", "Red", "White", "Yellow", "Purple", "Teal", "Multi-coloured", "Brown", "Grey", "Orange", "Black"]
    styles = ["Plain", "Stripe", "Check", "Polka dot", "Chevron", "Geometric", "Floral", "Illustration"]
    return render_template('fabrics/edit.html', fabric = fabric, all_manufacturers = manufacturers, all_colours = colours, all_styles = styles)


@fabrics_blueprint.route("/fabrics/<id>", methods=['POST'])
def update_fabric(id):
    manufacturer_id = request.form['manufacturer_id']
    design_ref = request.form['design_ref']
    main_colour = request.form['main_colour']
    style = request.form['style']
    stock_price = request.form['stock_price']
    sale_price = request.form['sale_price']
    quantity = request.form['quantity']
    manufacturer = manufacturer_repository.select(manufacturer_id)
    fabric = Fabric(manufacturer, design_ref, main_colour, style, stock_price, sale_price, quantity, id)
    fabric_repository.update(fabric)
    return redirect('/fabrics')

# @fabrics_blueprint.route("/fabrics", methods=['PUT'])
# def update_for_manufacturer_filter():
#     fabric_repository.filter(fabric)
#     return redirect("/fabrics")

