from sqlalchemy.sql.schema import ForeignKey
from resources.db.connection import db
from resources.helpers import date


class Answer(db.Model):
    __tablename__ = "answers"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)
    datetime = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, ForeignKey('users.id'))
    question_id = db.Column(db.Integer, ForeignKey('questions.id'))
    user = db.relationship('User')
    question = db.relationship('Question')

    def __init__(self, text, user_id, question_id):
        self.text = text
        self.datetime = date.now()
        self.user_id = user_id
        self.question_id = question_id

