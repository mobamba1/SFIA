from flask_wtf import FlaskForm #enable to add forms in the application
from wtforms import StringField, SubmitField, IntegerField #identifiers of what data is going to be used
from wtforms.validators import DataRequired, Length # validators to ensure that data is input correctly 

class AddForm(FlaskForm): #used to add a intake and burnt calorie
    burnt = StringField('Burnt Calories',
        validators = [
            DataRequired(),#ensure that the form needs to be filledi n
            Length(min=2, max=30)#makes sure that the data leng is between 2 and 30 
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
            Length(min=0,max =30)
        ]
    )
    submit = SubmitField('Post!')

class UpdateAddForm(FlaskForm): #update the current burnt and intake with new one
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
    calorie_id = StringField('Calorie ID',#this is the key to identify which data needs to be updated
        validators = [
            DataRequired(),
            Length(min=1, max=30)
        ]
    )
    submit = SubmitField('Update')
