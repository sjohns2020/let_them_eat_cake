from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.cake import Cake
from models.inventory import Inventory
import repositories.cake_repository as cake_repository
import repositories.baker_repository as baker_repository

cakes_blueprint = Blueprint("cakes", __name__)

@cakes_blueprint.route("/")
def landing():
    cakes = cake_repository.select_all()
    return render_template("index.html", all_cakes = cakes)

@cakes_blueprint.route("/dashboard")
def dashboard():
    cakes = cake_repository.select_all()
    low_stock_cakes = cake_repository.select_all_low_stock()
    return render_template("dashboard/index.html", all_cakes = cakes, low_stock_cakes = low_stock_cakes)
    



@cakes_blueprint.route("/cakes")
def cakes():
    cakes = cake_repository.select_all()
    bakers = baker_repository.select_all()
    return render_template("cakes/index.html", all_cakes = cakes, all_bakers = bakers)

# NEW
# GET '/cakes/new'
@cakes_blueprint.route("/cakes/new", methods=['GET'])
def new_cake():
    bakers = baker_repository.select_all()
    return render_template("/cakes/new.html", all_bakers = bakers)

# CREATE
# POST '/cakes'
@cakes_blueprint.route("/cakes",  methods=['POST'])
def create_cake():
    full_name = request.form['full_name']
    qty_on_hand = request.form['qty_on_hand']
    manufacture_cost = request.form['manufacture_cost']
    selling_price = request.form['selling_price']
    baker_id = request.form['baker_id']
    category = request.form['category']
    vegetarian = request.form['vegetarian']
    daily_sales_forecast = request.form['daily_sales_forecast']
    par_level = request.form['par_level']
    baker = baker_repository.select(baker_id)
    cake = Cake(full_name, qty_on_hand, manufacture_cost, selling_price, baker, category, vegetarian, daily_sales_forecast, par_level)
    cake_repository.save(cake)
    return redirect('/cakes')

# SHOW
# GET '/cakes/<id>'
@cakes_blueprint.route("/cakes/<id>", methods=['GET'])
def show_cake(id):
    cake = cake_repository.select(id)
    return render_template('cakes/show.html', cake = cake)

# EDIT
# GET '/cakes/<id>/edit'
@cakes_blueprint.route("/cakes/<id>/edit", methods=['GET'])
def edit_cake(id):
    cake = cake_repository.select(id)
    bakers = baker_repository.select_all()
    return render_template('cakes/edit.html', cake = cake, all_bakers = bakers)

# EDIT DETAILS
# GET '/cakes/<id>/edit'
@cakes_blueprint.route("/cakes/<id>/details", methods=['GET'])
def edit_cake_details(id):
    cake = cake_repository.select(id)
    bakers = baker_repository.select_all()
    return render_template('cakes/edit_details.html', cake = cake, all_bakers = bakers)



# UPDATE
# PUT '/cakes/<id>'
@cakes_blueprint.route("/cakes/<id>", methods=['POST'])
def update_cake(id):
    full_name = request.form['full_name']
    qty_on_hand = request.form['qty_on_hand']
    manufacture_cost = request.form['manufacture_cost']
    selling_price = request.form['selling_price']
    baker_id = request.form['baker_id']
    category = request.form['category']
    vegetarian = request.form['vegetarian']
    daily_sales_forecast = request.form['daily_sales_forecast']
    par_level = request.form['par_level']
    baker = baker_repository.select(baker_id)
    cake = Cake(full_name, qty_on_hand, manufacture_cost, selling_price, baker, category, vegetarian, daily_sales_forecast, par_level, id)
    cake_repository.update(cake)
    return redirect('/cakes')


# DELETE
# DELETE '/cakes/<id>'
@cakes_blueprint.route("/cakes/<id>/delete", methods=['POST'])
def delete_cake(id):
    cake_repository.delete(id)
    return redirect('/cakes')