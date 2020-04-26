from flask_wtf import FlaskForm
from wtforms import StringField, validators

class IngredientForm(FlaskForm):
    name = StringField("Ingredient name", [validators.Length(min=3)])
    unit = StringField("unit")
 
    class Meta:
        csrf = False
