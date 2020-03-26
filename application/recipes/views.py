from application import app, db
from flask import render_template, request, redirect, url_for
from application.recipes.models import Recipe
from application.recipes.forms import RecipeForm

@app.route("/recipes", methods=["GET"])
def recipes_index():
    return render_template("recipes/list.html", recipes = Recipe.query.all())

@app.route("/recipes/new/")
def recipes_form():
    return render_template("recipes/new.html", form = RecipeForm())

@app.route("/recipes/", methods=["POST"])
def recipes_create():
    form = RecipeForm(request.form)

    if not form.validate():
        return render_template("recipes/new.html", form = form)

    r = Recipe(form.name.data)
    r.favourite = form.favourite.data

    db.session().add(r)
    db.session().commit()
  
    return redirect(url_for("recipes_index"))

@app.route("/recipes/<recipe_id>/", methods=["POST"])
def recipes_set_favourite(recipe_id):

    r = Recipe.query.get(recipe_id)
    r.favourite = not r.favourite
    db.session().commit()
  
    return redirect(url_for("recipes_index"))
