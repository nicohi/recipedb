from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators

class ToolForm(FlaskForm):
    name = StringField("Tool name", [validators.Length(min=3)])
 
    class Meta:
        csrf = False
