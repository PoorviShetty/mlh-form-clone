from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Submission(db.Model):
    form_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False, nullable=False)
    university = db.Column(db.String(50), unique=False)
    skills = db.Column(db.String(50), unique=False)
    resume = db.Column(db.String(50), unique=False)

    def __repr__(self):
        return f"Name : {self.name}"