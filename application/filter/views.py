from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application.auth.models import User
from application.recipes.models import Recipe
from application.filter.models import Filter
from application.filter.forms import FilterForm, SearchForm
from application.ingredients.models import Ingredient
from application.recipes.forms import RecipeForm, IngredientWithRecipeForm

# search with string and filter object
def search(term, filt):
    if filt is None:
        filt = Filter(id = current_user.id)
    if term is None:
        term = ""

    term = term.lower()

    def filterByTerm(r):
        return (term in r.name.lower()
            or term in r.description.lower()
            or term in r.text.lower())

    if len(filt.ingredients) == 0:
        return filter(filterByTerm, Recipe.query.all())

    #rs = Recipe.query.filter(Recipe.id.in_(filt.get_recipes(filt))).all()
    rs = filt.get_recipes(filt)
    return filter(filterByTerm, rs)

@app.route("/filter", methods=["GET"])
@login_required
def filter_index():
    form = FilterForm()
    form.ingredient.choices = map(lambda i: (i.id, i.name), Ingredient.query.all())
    f = Filter.query.get(Filter.get_filter(current_user.id))
    rs = search(request.args.get('term'), f)
    ings = Ingredient.query.all(),
    if f is None:
        return render_template("filter/list.html",  recipes = rs, form = form)
    return render_template("filter/list.html",  recipes = rs, form = form, ingredients = f.ingredients)

@app.route("/filter/add", methods=["POST"])
@login_required
def filter_add_ingredient():
    form = FilterForm(request.form)
    f = Filter.query.get(Filter.get_filter(current_user.id))
    usr = User.query.get(current_user.id)
    if f is None:
        f = Filter(id = current_user.id)
        usr.filter_id = f.id
        db.session().add(f)

    f.ingredients.append(Ingredient.query.get(form.ingredient.data))
    db.session().commit()
  
    return redirect(url_for("filter_index"))

@app.route("/filter/del/<ingredient_id>", methods=["POST"])
@login_required
def filter_del_ingredient(ingredient_id):
    f = Filter.query.get(Filter.get_filter(current_user.id))
    f.ingredients.remove(Ingredient.query.get(ingredient_id))
    db.session().commit()
    return redirect(url_for("filter_index"))
