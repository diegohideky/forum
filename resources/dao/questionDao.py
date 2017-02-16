from resources.db.connection import db
from resources.models.question import Question


def insert(question):
    db.session.add(question)
    db.session.commit()


def delete(question):
    db.session.delete(question)
    db.session.commit()


def find():
    return db.session.query(Question).order_by(Question.datetime.desc()).all()


def findById(id):
    return Question.query.get(id)


def findByUserId(id):
    return db.session.query(Question).filter(Question.user_id==id).order_by(Question.datetime.desc()).all()

