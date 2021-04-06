from flask import Flask, render_template, url_for, redirect, request
from flask import Blueprint

from models.fabric import Fabric
from models.manufacturer import Manufacturer

import repositories.fabric_repository as fabric_repository
import repositories.manufacturer_repository as manufacturer_repository

manufacturers_blueprint = Blueprint("manufacturers", __name__)

@manufacturers_blueprint.route("/manufacturers")
def manufacturers():
    manufacturers = manufacturer_repository.select_all()
    return render_template("/manufacturers/index.html", manufacturers = manufacturers)


@manufacturers_blueprint.route("/manufacturer/<id>")
def show_manufacturer(id):
    manufacturer = manufacturer_repository.select(id)
    return render_template("/manufacturers/show.html", manufacturer = manufacturer)


@manufacturers_blueprint.route("/manufacturers", methods =['GET'])
def new_manufacturer():
    return render_template("/manufacturers/index.html")


@manufacturers_blueprint.route("/manufacturers/new", methods=['POST'])
def create_manufacturer():
    name = request.form['name']
    sales_contact = request.form['sales_contact']
    active = request.form['active']
    manufacturer = Manufacturer(name, sales_contact, active)
    manufacturer_repository.save(manufacturer)
    return redirect("/manufacturers")

@manufacturers_blueprint.route("/manufacturers/<id>/delete-manufacturer", methods = ['POST'])
def delete_manufacturer(id):
    manufacturer_repository.delete(id)
    return redirect("/manufacturers")


@manufacturers_blueprint.route("/manufacturers/<id>/edit", methods=['GET'])
def edit_manufacturer(id):
    manufacturer = manufacturer_repository.select(id)
    return render_template('manufacturers/edit.html', manufacturer = manufacturer)


@manufacturers_blueprint.route("/manufacturers/<id>", methods=['POST'])
def update_manufacturer(id):
    name = request.form['name']
    sales_contact = request.form['sales_contact']
    active = request.form['active']
    manufacturer = Manufacturer(name, sales_contact, active, id)
    manufacturer_repository.update(manufacturer)
    return redirect('/manufacturers')