from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SelectMultipleField, validators

ingredients = [('0', 'Cheese'),
                ('1', 'Eggs'),
                ('3', 'Milk'),
                ('2', 'Flour')]

tools = [('0', 'Grill'),
                ('1', 'Microwave'),
                ('3', 'Pan'),
                ('2', 'Pot')]

class RecipeForm(FlaskForm):
    name = StringField("Recipe name", [validators.Length(min=3)])
    favourite = BooleanField("Favourite")

    ingredients = SelectMultipleField(u'Ingredients', choices=ingredients)
    tools = SelectMultipleField(u'Tools', choices=tools)

    text = StringField("Recipe text")
 
    class Meta:
        csrf = False
