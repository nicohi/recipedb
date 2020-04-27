from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, IntegerField, validators

class RecipeForm(FlaskForm):
    name = StringField("Recipe name", [validators.Length(min=3)])
    favourite = BooleanField("Favourite")

    text = StringField("Recipe text")
 
    class Meta:
        csrf = False

class IngredientWithRecipeForm(FlaskForm):
    ingredient = SelectField("Add", choices=[(0,"EMPTY")])
    quantity = IntegerField("quantity")
 
    class Meta:
        csrf = False
