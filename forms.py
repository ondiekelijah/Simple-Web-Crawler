from wtforms import StringField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired


class Url(FlaskForm):
    urltext = StringField(validators=[InputRequired()])
    specificElement = StringField(validators=[InputRequired()])
