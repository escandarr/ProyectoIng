from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AudioForm(FlaskForm):
    name = StringField('Audio Name', validators=[DataRequired()])
    client_name = StringField('Client Name', validators=[DataRequired()])
    campaign_name = StringField('Campaign Name', validators=[DataRequired()])
    submit = SubmitField('Upload')
