from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SelectMultipleField, validators

class RecipeForm(FlaskForm):
    name = StringField("Recipe name", [validators.Length(min=3)])
    favourite = BooleanField("Favourite")

    ingredients = SelectMultipleField(u'Ingredients', choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')])
    tools = SelectMultipleField(u'Tools', choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')])

    text = StringField("Recipe text")
 
    class Meta:
        csrf = False
