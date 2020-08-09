from application import db #child of db

class Adding(db.Model): #creates a table for SQL with these parameters
    id = db.Column(db.Integer, primary_key=True)
    burnt = db.Column(db.String(30), nullable=False)
    intake = db.Column(db.String(30), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id')) # this is take from teh user table as the foreign key
    def __repr__(self):
        return ''.join([
            'Burnt: ', self.burnt, '\r\n',
            'Intake: ', self.intake
            ])

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    daily = db.relationship('Adding', backref='owner') # this is the relationship between user and adding
