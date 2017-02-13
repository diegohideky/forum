from resources.db.connection import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    type = db.Column(db.String)
    questions = db.relationship('Question', backref='questions', cascade='all, delete-orphan', lazy='dynamic')

    def __init__(self, username, password, type):
        self.username = username
        self.password = password
        self.type = type

