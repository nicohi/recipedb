from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application.recipes.models import Recipe
from application.ingredients.models import Ingredient
from application.recipes.forms import RecipeForm, IngredientWithRecipeForm

import re

# remove most special symbols from string (except ,.-)
def cleanstr(s):
    ret = ""
    for k in s.split("\n"):
        ret = ret + re.sub(r"[^a-zA-Z0-9.,-]+", ' ', k) + '\n'
    return ret

@app.route("/recipes", methods=["GET"])
def recipes_index():
    return render_template("recipes/list.html", recipes = Recipe.query.all())

@app.route("/recipes/new/")
@login_required
def recipes_form():
    return render_template("recipes/new.html", form = RecipeForm())

@app.route("/recipes/", methods=["POST"])
@login_required
def recipes_create():
    form = RecipeForm(request.form)

    if not form.validate():
        return render_template("recipes/new.html", form = form)

    r = Recipe(form.name.data)
    r.favourite = form.favourite.data
    r.account_id = current_user.id
    r.description = cleanstr(form.description.data)

    db.session().add(r)
    db.session().commit()
  
    return redirect(url_for("recipes_index"))

@app.route("/recipes/<recipe_id>/edit", methods=["POST"])
@login_required
def recipes_edit(recipe_id):
    form = RecipeForm(request.form)
    r = Recipe.query.get(recipe_id)

    if not form.validate():
        return redirect(url_for("recipes_view", recipe_id=recipe_id, form = form))

    r.name = form.name.data
    r.favourite = form.favourite.data
    r.description = cleanstr(form.description.data)
    r.text = cleanstr(form.text.data)

    db.session().commit()
  
    return redirect(url_for("recipes_view",recipe_id=recipe_id))

@app.route("/recipes/<recipe_id>/ingredient", methods=["POST"])
@login_required
def recipes_add_ingredient(recipe_id):
    form = IngredientWithRecipeForm(request.form)
    r = Recipe.query.get(recipe_id)

    quantity = form.quantity.data
    try:
        quantity = int(quantity)
    except:
        quantity = 0

    r.ingredients.append(Ingredient.query.get(form.ingredient.data))
    db.session().commit()

    r.set_quantity(r, form.ingredient.data, quantity)

    return redirect(url_for("recipes_editpage",recipe_id=recipe_id))

@app.route("/recipes/<recipe_id>/ingredient/<ingredient_id>", methods=["POST"])
@login_required
def recipes_del_ingredient(recipe_id, ingredient_id):
    r = Recipe.query.get(recipe_id)
    r.ingredients.remove(Ingredient.query.get(ingredient_id))
    db.session().commit()

    return redirect(url_for("recipes_view",recipe_id=recipe_id))

@app.route("/recipes/<recipe_id>/", methods=["GET"])
@login_required
def recipes_editpage(recipe_id):
    r = Recipe.query.get(recipe_id)
    f = RecipeForm(obj = Recipe.query.get(recipe_id))
    f2 = IngredientWithRecipeForm()
    f2.ingredient.choices = map(lambda i: (i.id, i.name+" ({})".format(i.unit)), Ingredient.query.order_by(Ingredient.name).all())
    ings = map(lambda i: [i, r.get_quantity(r,i.id)], r.ingredients)
    return render_template("recipes/recipe.html", form = f, form2 = f2, r = r, ingredients = ings)

@app.route("/recipes/<recipe_id>/view", methods=["GET"])
def recipes_view(recipe_id):
    r = Recipe.query.get(recipe_id)
    ings = map(lambda i: [i, r.get_quantity(r,i.id)], r.ingredients)
    return render_template("recipes/view.html", r = r, ingredients = ings)

@app.route("/recipes/<recipe_id>/", methods=["POST"])
@login_required
def recipes_set_favourite(recipe_id):

    r = Recipe.query.get(recipe_id)
    r.favourite = not r.favourite
    db.session().commit()
  
    return redirect(url_for("recipes_view", recipe_id=recipe_id))

@app.route("/recipes/<recipe_id>/del", methods=["POST"])
@login_required
def recipes_delete(recipe_id):

    r = Recipe.query.get(recipe_id)
    db.session().delete(r)
    db.session().commit()
  
    return redirect(url_for("recipes_view", recipe_id=recipe_id))
