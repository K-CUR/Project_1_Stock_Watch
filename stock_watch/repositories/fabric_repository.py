from db.run_sql import run_sql

from models.fabric import Fabric
from models.manufacturer import Manufacturer

import repositories.manufacturer_repository as manufacturer_repository


def save(fabric):
    sql = "INSERT INTO fabrics (manufacturer_id, design_ref, main_colour, style, stock_price, sale_price, quantity) VALUES ( %s, %s, %s, %s, %s, %s, %s ) RETURNING id"
    values = [fabric.manufacturer.id, fabric.design_ref, fabric.main_colour, fabric.style, fabric.stock_price, fabric.sale_price, fabric.quantity]
    results = run_sql(sql, values)
    id = results [0] ['id']
    fabric.id = id
    return fabric


def delete_all():
    sql = "DELETE from fabrics"
    run_sql(sql)


def select_all():
    fabrics = []

    sql = "SELECT * FROM fabrics"
    results = run_sql(sql)

    for row in results:
        manufacturer = manufacturer_repository.select(row['manufacturer_id'])
        fabric = Fabric(manufacturer, row['design_ref'], row['main_colour'], row ['style'], row['stock_price'], row['sale_price'], row['quantity'], row['id'])
        fabrics.append(fabric)
    return fabrics


def select(id):
    fabric = None

    sql = "SELECT * FROM fabrics WHERE id = %s"
    values = [id]
    result = run_sql(sql, values) [0]

    if result is not None:
        manufacturer = manufacturer_repository.select(result['manufacturer_id'])
        fabric = Fabric(manufacturer, result['design_ref'], result['main_colour'], result['style'], result['stock_price'], result['sale_price'], result['quantity'], result['id'])
    return fabric


def delete(id):
    sql = "DELETE FROM fabrics WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)


def update(fabric):
    sql = "UPDATE fabrics SET (manufacturer_id, design_ref, main_colour, style, stock_price, sale_price, quantity) = ( %s, %s, %s, %s, %s, %s, %s ) WHERE id = %s"
    values = [fabric.manufacturer.id, fabric.design_ref, fabric.main_colour, fabric.style, fabric.stock_price, fabric.sale_price, fabric.quantity, fabric.id]
    run_sql(sql, values)


def filter_fabric_by_fields(manufacturer_id, colour):
    # have the id from the filter form
    fabrics = []

    sql = "SELECT * FROM fabrics WHERE manufacturer_id = %s AND main_colour = %s"
    values = [manufacturer_id, colour]
    results = run_sql(sql, values)

    for row in results:
        manufacturer = manufacturer_repository.select(manufacturer_id)

        fabric = Fabric(manufacturer, row['design_ref'], row['main_colour'], row ['style'], row['stock_price'], row['sale_price'], row['quantity'], row['id'])
        fabrics.append(fabric)
    return fabrics


def filter_fabric_by_colour(colour):
    # have the id from the filter form
    fabrics = []

    sql = "SELECT * FROM fabrics WHERE main_colour = %s"
    values = [colour]
    results = run_sql(sql, values)

    for row in results:
        manufacturer = manufacturer_repository.select(row['manufacturer_id'])

        fabric = Fabric(manufacturer, row['design_ref'], row['main_colour'], row ['style'], row['stock_price'], row['sale_price'], row['quantity'], row['id'])
        fabrics.append(fabric)
    return fabrics


def filter_fabric_by_manufacturer(manufacturer_id):
    # have the id from the filter form
    fabrics = []

    sql = "SELECT * FROM fabrics WHERE manufacturer_id = %s"
    values = [manufacturer_id]
    results = run_sql(sql, values)

    for row in results:
        manufacturer = manufacturer_repository.select(manufacturer_id)

        fabric = Fabric(manufacturer, row['design_ref'], row['main_colour'], row ['style'], row['stock_price'], row['sale_price'], row['quantity'], row['id'])
        fabrics.append(fabric)
    return fabrics
