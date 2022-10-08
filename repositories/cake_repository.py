from db.run_sql import run_sql

from models.cake import Cake
from models.baker import Baker
import repositories.baker_repository as baker_repository


def save(cake):
    sql = "INSERT INTO cakes (full_name , qty_on_hand, manufacture_cost, selling_price, baker_id, category, vegetarian, daily_sales_forecast, par_level) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [cake.full_name, cake.qty_on_hand, cake.manufacture_cost, cake.manufacture_cost, cake.baker.id, cake.category, cake.vegetarian, cake.daily_sales_forecast, cake.par_level]
    results = run_sql(sql, values)
    id = results[0]['id']
    cake.id = id
    return cake


def select_all():
    cakes = []

    sql = "SELECT * FROM cakes"
    results = run_sql(sql)

    for row in results:
        baker = baker_repository.select(row['baker_id'])
        cake = Cake (row['full_name'], row['qty_on_hand'], row['manufacture_cost'], row['manufacture_cost'], baker, row['category'], row['vegetarian'], row['daily_sales_forecast'], row['par_level'], row['id'] )
        cakes.append(cake)
    return cakes



def select(id):
    cake = None
    sql = "SELECT * FROM cakes WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        baker = baker_repository.select(result['baker_id'])
        cake = Cake(result['full_name'], result['qty_on_hand'], result['manufacture_cost'], result['selling_price'], baker, result['category'], result['vegetarian'], result['daily_sales_forecast'], result['par_level'], result['id'] )
    return cake


def delete_all():
    sql = "DELETE  FROM cakes"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM cakes WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(cake):
    sql = "(full_name , qty_on_hand, manufacture_cost, selling_price, baker_id, category, vegetarian, daily_sales_forecast, par_level) = (%s, %s, %s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values =  [cake.full_name, cake.qty_on_hand, cake.manufacture_cost, cake.manufacture_cost, cake.baker.id, cake.category, cake.vegetarian, cake.daily_sales_forecast, cake.par_level]
    run_sql(sql, values)