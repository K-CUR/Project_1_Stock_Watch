from db.run_sql import run_sql

from models.manufacturer import Manufacturer
from models.fabric import Fabric

import repositories.fabric_repository as fabric_repository


def save(manufacturer):
    sql = "INSERT INTO manufacturers (manufacturer_name, sales_contact, active) VALUES ( %s, %s, %s) RETURNING id"
    values = [manufacturer.name, manufacturer.sales_contact, manufacturer.active]
    results = run_sql(sql, values)
    id = results [0] ['id']
    manufacturer.id = id
    return manufacturer


def delete_all():
    sql = "DELETE from manufacturers"
    run_sql(sql)


def select_all():
    manufacturers = []

    sql = "SELECT * FROM manufacturers"
    results = run_sql(sql)

    for row in results:
        manufacturer = Manufacturer(row['manufacturer_name'], row['sales_contact'], row['active'], row['id'])
        manufacturers.append(manufacturer)
    return manufacturers


def select(id):
    manufacturer = None

    sql = "SELECT * FROM manufacturers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values) [0]

    if result is not None:
        manufacturer = Manufacturer(result['manufacturer_name'], result['sales_contact'], result['active'], result['id'])
        # had error 'row not defined' because I had row[] instead of result[]
    return manufacturer


def delete(id):
    sql = "DELETE FROM manufacturers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)


def update(manufacturer):
    sql = "UPDATE manufacturers SET (manufacturer_name, sales_contact, active) = ( %s, %s, %s ) WHERE id = %s"
    values = [manufacturer.name, manufacturer.sales_contact, manufacturer.active]
    run_sql(sql, values)


def fabrics(manufacturer):
    fabrics = []

    sql = "SELECT * FROM fabrics WHERE manufacturer_id = %s"
    values = [manufacturer.id]
    results = run_sql(sql, values)

    for row in results:
        fabric = Fabric(manufacturer, row['design_ref'], row['main_colour'], row ['style'], row['stock_price'], row['sale_price'], row['quantity'], row['id'])
        fabrics.append(fabric)
    return fabrics


def select_active():
    manufacturers = []

    sql = "SELECT * FROM manufacturers WHERE active = %s"
    values = [True]
    results = run_sql(sql, values)

    for row in results:
        manufacturer = Manufacturer(row['manufacturer_name'], row['sales_contact'], row['active'], row['id'])
        manufacturers.append(manufacturer)
    return manufacturers