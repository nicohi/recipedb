from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators

class RecipeForm(FlaskForm):
    name = StringField("Recipe name", [validators.Length(min=3)])
    favourite = BooleanField("Favourite")
 
    class Meta:
        csrf = False
