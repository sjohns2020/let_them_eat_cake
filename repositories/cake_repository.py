from db.run_sql import run_sql

from models.cake import Cake
from models.baker import Baker
import repositories.baker_repository as baker_repository


def save(cake):
    sql = "INSERT INTO cakes (description, baker_id, duration, completed) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [cake.description, cake.baker.id, cake.duration, cake.completed]
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
        cake = Cake(row['description'], baker, row['duration'], row['completed'], row['id'] )
        cakes.append(cake)
    return cakes



def select(id):
    cake = None
    sql = "SELECT * FROM cakes WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    # checking if the list returned by `run_sql(sql, values)` is empty. Empty lists are 'fasly' 
    # Could alternativly have..
    # if len(results) > 0 
    if results:
        result = results[0]
        baker = baker_repository.select(result['baker_id'])
        cake = Cake(result['description'], baker, result['duration'], result['completed'], result['id'] )
    return cake


def delete_all():
    sql = "DELETE  FROM cakes"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM cakes WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(cake):
    sql = "UPDATE cakes SET (description, baker_id, duration, completed) = (%s, %s, %s, %s) WHERE id = %s"
    values = [cake.description, cake.baker.id, cake.duration, cake.completed, cake.id]
    run_sql(sql, values)