from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application.recipes.models import Recipe
from application.recipes.forms import RecipeForm

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

    db.session().add(r)
    db.session().commit()
  
    return redirect(url_for("recipes_index"))

@app.route("/recipes/<recipe_id>/edit", methods=["POST"])
@login_required
def recipes_edit(recipe_id):
    form = RecipeForm(request.form)

    r = Recipe.query.get(recipe_id)

    if not form.validate():
        return render_template("recipes/"+recipe_id, form = form)

    r.name = form.name.data
    r.favourite = form.favourite.data
    #r.account_id = current_user.id

    db.session().commit()
  
    return redirect(url_for("recipes_index"))

@app.route("/recipes/<recipe_id>/", methods=["GET"])
@login_required
def recipes_view(recipe_id):
    r = Recipe.query.get(recipe_id)
    f = RecipeForm(obj = Recipe.query.get(recipe_id))
    return render_template("recipes/recipe.html", form = f, r = r)

@app.route("/recipes/<recipe_id>/", methods=["POST"])
@login_required
def recipes_set_favourite(recipe_id):

    r = Recipe.query.get(recipe_id)
    r.favourite = not r.favourite
    db.session().commit()
  
    return redirect(url_for("recipes_index"))

@app.route("/recipes/<recipe_id>/del", methods=["POST"])
@login_required
def recipes_delete(recipe_id):

    r = Recipe.query.get(recipe_id)
    db.session().delete(r)
    db.session().commit()
  
    return redirect(url_for("recipes_index"))
