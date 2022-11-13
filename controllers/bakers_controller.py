from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.baker import Baker
import repositories.baker_repository as baker_repository
import repositories.baker_repository as baker_repository

bakers_blueprint = Blueprint("bakers", __name__)

@bakers_blueprint.route("/bakers")
def bakers():
    bakers = baker_repository.select_all()
    return render_template("bakers/index.html", all_bakers = bakers)

# NEW
# GET '/bakers/new'
@bakers_blueprint.route("/bakers/new", methods=['GET'])
def new_baker():
    bakers = baker_repository.select_all()
    return render_template("bakers/new.html", all_bakers = bakers)

# CREATE
# POST '/bakers'
@bakers_blueprint.route("/bakers",  methods=['POST'])
def create_baker():
    full_name = request.form['full_name']
    favourite_quote = request.form['favourite_quote']
    length_of_service = request.form['length_of_service']
    salary = request.form['salary']
    baker = Baker(full_name, favourite_quote, length_of_service, salary)
    baker_repository.save(baker)
    return redirect('/bakers')

# SHOW
# GET '/bakers/<id>'
@bakers_blueprint.route("/bakers/<id>", methods=['GET'])
def show_baker(id):
    baker = baker_repository.select(id)
    return render_template('bakers/edit.html', baker = baker)

# EDIT
# GET '/bakers/<id>/edit'
@bakers_blueprint.route("/bakers/<id>/edit", methods=['GET'])
def edit_baker(id):
    baker = baker_repository.select(id)
    bakers = baker_repository.select_all()
    return render_template('bakers/edit.html', baker = baker, all_bakers = bakers)

# UPDATE
# PUT '/bakers/<id>'
@bakers_blueprint.route("/bakers/<id>", methods=['POST'])
def update_baker(id):
    full_name = request.form['full_name']
    favourite_quote = request.form['favourite_quote']
    length_of_service = request.form['length_of_service']
    salary = request.form['salary']
    baker = Baker(full_name, favourite_quote, length_of_service, salary, id)
    baker_repository.update(baker)
    return redirect('/bakers')

# DELETE
# DELETE '/bakers/<id>'
@bakers_blueprint.route("/bakers/<id>/delete", methods=['POST'])
def delete_baker(id):
    baker_repository.delete(id)
    return redirect('/bakers')