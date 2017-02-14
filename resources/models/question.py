from sqlalchemy.sql.schema import ForeignKey
from resources.db.connection import db
from resources.helpers import date


class Question(db.Model):
    __tablename__ = "questions"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)
    datetime = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, ForeignKey('users.id'))
    user = db.relationship('User')
    answers = db.relationship('Answer', backref='answers', cascade='all, delete-orphan', lazy='dynamic')

    def __init__(self, text, user_id):
        self.text = text
        self.datetime = date.now()
        self.user_id = user_id

