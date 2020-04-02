from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators

class IngredientForm(FlaskForm):
    name = StringField("Ingredient name", [validators.Length(min=3)])
 
    class Meta:
        csrf = False
