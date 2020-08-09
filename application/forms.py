from flask_wtf import FlaskForm #flask forms so that it can be included in the front end
from wtforms import StringField, SubmitField #this will used to identify the type of data being placed
from wtforms.validators import DataRequired, Length #ensure that validators are used correctly so that no data is left out 

class AddForm(FlaskForm): # this form is to add new burnt and intake calories by the user
    burnt = StringField('Burnt Calories',
        validators = [
            DataRequired(),#data needs to be inputed through the forms
            Length(min=2, max=30)#data has to be min 2 length and 30 max
        ]
    )
    intake = StringField('Caloric Intake',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    submit = SubmitField('Post!')

class UpdateAddForm(FlaskForm): # this is to update the data in SQL
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
    submit = SubmitField('Update')
