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


def select_all():
    manufacturers = []

    sql = "SELECT * FROM manufacturers"
    results = run_sql(sql)

    for row in results:
        Manufacturer = Manufacturer(row['name'], row['sales_contact'], row['active'], row['id'])
        manufacturers.append(manufacturer)
    return manufacturers


def select(id):
    manufacturer = None

    sql = "SELECT * FROM manufacturers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values) [0]

    if result is not None:
        manufacturer = Manufacturer(row['name'], row['sales_contact'], row['active'], row['id'])
    return manufacturer


def delete(id):
    sql = "DELETE FROM manufacturers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)


def update(fabric):
    sql = "UPDATE manufacturers SET (name, sales_contact, active) = ( %s, %s, %s ) WHERE id = %s"
    values = [manufacturer.name, manufacturer.sales_contact, manufacturer.active]
    run_sql(sql, values)