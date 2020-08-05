from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class AddForm(FlaskForm):
    burnt = StringField('Burnt Calories',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    intake = StringField('Caloric Intake',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    submit = SubmitField('Post!')
