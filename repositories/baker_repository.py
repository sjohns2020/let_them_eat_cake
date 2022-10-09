from db.run_sql import run_sql

from models.baker import Baker
from models.cake import Cake


def save(baker):
    sql = "INSERT INTO bakers (full_name, favourite_quote, length_of_service, salary) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [baker.full_name, baker.favourite_quote, baker.length_of_service, baker.salary]
    results = run_sql(sql, values)
    id = results[0]['id']
    baker.id = id
    return baker


def select_all():
    bakers = []

    sql = "SELECT * FROM bakers"
    results = run_sql(sql)

    for row in results:
        baker = Baker(row['full_name'], row['favourite_quote'], row['length_of_service'], row['salary'], row['id'] )
        bakers.append(baker)
    return bakers


def select(id):
    baker = None
    sql = "SELECT * FROM bakers WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        baker = Baker(result['full_name'], result['favourite_quote'], result['length_of_service'], result['salary'], result['id'] )
    return baker


def delete_all():
    sql = "DELETE  FROM bakers"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM bakers WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(baker):
    sql = "UPDATE bakers SET (full_name, favourite_quote, length_of_service, salary) = (%s, %s, %s, %s) WHERE id = %s"
    values =  [baker.full_name, baker.favourite_quote, baker.length_of_service, baker.salary, baker.id]
    run_sql(sql, values)

def cakes(baker):
    cakes = []

    sql = "SELECT * FROM cakes WHERE baker_id = %s"
    values = [baker.id]
    results = run_sql(sql, values)

    for row in results:
        cake = Cake(row['full_name'], row['qty_on_hand'], row['manufacture_cost'], row['selling_price'], row['baker_id'], row['category'], row['vegetarian'], row['daily_sales_forecast'], row['par_level'], row['id'] )
        cakes.append(cake)
    return cakes