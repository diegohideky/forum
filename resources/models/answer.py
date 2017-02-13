from sqlalchemy.sql.schema import ForeignKey
from resources.db.connection import db


class Answer(db.Model):
    __tablename__ = "answers"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)
    data = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, ForeignKey('users.id'))
    question_id = db.Column(db.Integer, ForeignKey('questions.id'))
    user = db.relationship('User')
    question = db.relationship('Question')

    def __init__(self, text, data, user_id, question_id):
        self.text = text
        self.data = data
        self.user_id = user_id
        self.question_id = question_id

