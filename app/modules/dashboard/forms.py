from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class DashboardForm(FlaskForm):
    ndatasets = StringField('Number', validators=[DataRequired()])