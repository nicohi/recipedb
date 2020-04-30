from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application.ingredients.models import Ingredient
from application.ingredients.forms import IngredientForm

@app.route("/ingredients", methods=["GET"])
@login_required
def ingredients_index():
    return render_template("ingredients/list.html", ingredients = Ingredient.query.all())

@app.route("/ingredients/new/")
@login_required
def ingredients_form():
    return render_template("ingredients/new.html", form = IngredientForm())

@app.route("/ingredients/", methods=["POST"])
@login_required
def ingredients_create():
    form = IngredientForm(request.form)

    if not form.validate():
        return render_template("ingredients/new.html", form = form)

    i = Ingredient(form.name.data)
    i.account_id = current_user.id
    i.unit = form.unit.data

    db.session().add(i)
    db.session().commit()
  
    return redirect(url_for("ingredients_index"))

@app.route("/ingredients/<ingredient_id>/edit", methods=["POST"])
@login_required
def ingredients_edit(ingredient_id):
    form = IngredientForm(request.form)

    i = Ingredient.query.get(ingredient_id)

    if not form.validate():
        return render_template("ingredients/"+ingredient_id, form = form)

    i.name = form.name.data
    i.account_id = current_user.id
    i.unit = form.unit.data

    db.session().commit()
  
    return redirect(url_for("ingredients_index"))

@app.route("/ingredients/<ingredient_id>/", methods=["GET"])
@login_required
def ingredients_view(ingredient_id):
    r = Ingredient.query.get(ingredient_id)
    f = IngredientForm(obj = Ingredient.query.get(ingredient_id))
    return render_template("ingredients/ingredient.html", form = f, r = r)

@app.route("/ingredients/<ingredient_id>/del", methods=["POST"])
@login_required
def ingredients_delete(ingredient_id):

    r = Ingredient.query.get(ingredient_id)
    db.session().delete(r)
    db.session().commit()
  
    return redirect(url_for("ingredients_index"))
