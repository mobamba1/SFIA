from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
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
    owner_id = StringField('Owner',
        validators = [
            DataRequired(),
            Length(min=1, max=30)
        ]
    )
    submit = SubmitField('Post!')

class UpdateAddForm(FlaskForm):
    burnt = StringField('Update Burnt Calories',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    intake = StringField('Update Caloric Intake',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    calorie_id = StringField('Calorie ID',
        validators = [
            DataRequired(),
            Length(min=1, max=30)
        ]
    )
    submit = SubmitField('Update')
