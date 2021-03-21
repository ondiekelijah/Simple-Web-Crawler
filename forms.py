from wtforms import (
    StringField,
    TextAreaField,
)
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import InputRequired, Length, EqualTo, Email, Regexp



class Url(FlaskForm):
    urltext = StringField()
    specificElement = StringField()
