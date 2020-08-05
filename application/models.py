from application import db

class Adding(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    burnt = db.Column(db.String(30), nullable=False)
    intake = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return ''.join([
            'Burnt: ', self.burnt, '\r\n',
            'Intake: ', self.intake
            ])
