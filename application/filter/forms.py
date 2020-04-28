from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, BooleanField, IntegerField, validators

class FilterForm(FlaskForm):
    ingredient = SelectField("Add", choices=[(0,"EMPTY")])
    class Meta:
        csrf = False

class SearchForm(FlaskForm):
    term = StringField("search")
    class Meta:
        csrf = False
