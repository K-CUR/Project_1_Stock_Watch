from db.run_sql import run_sql


from models.manufacturer import Manufacturer

def save(manufacturer):
    sql = "INSERT INTO manufacturers (name, sales_contact, active) VALUES ( %s, %s, %s ) RETURNING id"
    values = [manufacturer.name, manufacturer.sales_contact, manufacturer.active]
    results = run_sql(sql, values)
    id = results [0] ['id']
    manufacturer.id = id
    return manufacturer

def delete_all():
    sql = "DELETE from manufacturers"
    run_sql(sql)