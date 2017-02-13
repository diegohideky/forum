from sqlalchemy.sql.schema import ForeignKey
from resources.db.connection import db


class Question(db.Model):
    __tablename__ = "questions"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)
    data = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, ForeignKey('users.id'))
    user = db.relationship('User')
    answers = db.relationship('Answer', backref='answers', cascade='all, delete-orphan', lazy='dynamic')

    def __init__(self, text, data, user_id):
        self.text = text
        self.data = data
        self.user_id = user_id

