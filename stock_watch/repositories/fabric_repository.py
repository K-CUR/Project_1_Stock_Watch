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
        fabric = Fabric(row['manufacturer_id'], row['design_ref'], row['main_colour'], row ['style'], row['stock_price'], row['sale_price'], row['quantity'], row['id'])
        fabrics.append(fabric)
    return fabrics


    def select(id):
        fabric = None

        sql = "SELECT * FROM fabrics WHERE id = %s"
        values = [id]
        result = run_sql(sql, values) [0]

        if result is not None:
            fabric = Fabric(row['manufacturer_id'], row['design_ref'], row['main_colour'], row ['style'], row['stock_price'], row['sale_price'], row['quantity'], row['id'])
        return fabric


    def delete(id):
        sql = "DELETE FROM fabrics WHERE id = %s"
        values = [id]
        result = run_sql(sql, values)


    def update(fabric):
        sql = "UPDATE fabrics SET (manufacturer_id, design_ref, main_colour, style, stock_price, sale_price, quantity) = ( %s, %s, %s, %s, %s, %s, %s ) WHERE id = %s"
        values = [fabric.manufacturer.id, fabric.design_ref, fabric.main_colour, fabric.style, fabric.stock_price, fabric.sale_price, fabric.quantity]
        run_sql(sql, values) 