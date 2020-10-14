from flask_wtf import FlaskForm
from wtforms import SubmitField, BooleanField
from wtforms.validators import DataRequired

class RequestButton(FlaskForm):
    sendReq = BooleanField('Send Request to Server', validators=[DataRequired()])
    submit = SubmitField('Send Request to Server')