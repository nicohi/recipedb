from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, BooleanField, IntegerField, validators

class RecipeForm(FlaskForm):
    name = StringField("Recipe name", [validators.Length(min=3)])
    favourite = BooleanField("Favourite")

    description = StringField("Description")

    text = TextAreaField("Instructions")
 
    class Meta:
        csrf = False

class IngredientWithRecipeForm(FlaskForm):
    ingredient = SelectField("Add", choices=[(0,"EMPTY")])
    quantity = IntegerField("quantity")
 
    class Meta:
        csrf = False
