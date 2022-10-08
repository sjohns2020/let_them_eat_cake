# from flask import Flask, render_template, request, redirect
# from flask import Blueprint
# from models.baker import Baker
# import repositories.baker_repository as baker_repository

# bakers_blueprint = Blueprint("bakers", __name__)

# @bakers_blueprint.route("/bakers")
# def bakers():
#     bakers = baker_repository.select_all() # NEW
#     return render_template("bakers/index.html", bakers = bakers)

# @bakers_blueprint.route("/bakers/<id>")
# def show(id):
#     baker = baker_repository.select(id)
#     locations = baker_repository.locations(baker)
#     return render_template("bakers/show.html", baker=baker, locations=locations)