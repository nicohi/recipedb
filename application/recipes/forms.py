from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, IntegerField, validators

class RecipeForm(FlaskForm):
    name = StringField("Recipe name", [validators.Length(min=3)])
    favourite = BooleanField("Favourite")

    text = StringField("Recipe text")
 
    class Meta:
        csrf = False

class IngredientWithRecipeForm(FlaskForm):
    ingredient = SelectField("Ingredient", choices=[(0,"EMPTY")])
    quantity = IntegerField("quantity", default=0)
 
    class Meta:
        csrf = False
