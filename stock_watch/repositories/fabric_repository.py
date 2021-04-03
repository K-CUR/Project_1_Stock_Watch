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

