from operator import imod
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, InputRequired
from wtforms import SubmitField

class SubmitImageForm(FlaskForm):
    picture = FileField('Submit new image', validators=[FileAllowed(['jpg', 'png',]), InputRequired()])
    submit = SubmitField('Submit')
