from resources.db.connection import db
from resources.models.answer import Answer


def insert(answer):
    db.session.add(answer)
    db.session.commit()


def delete(answer):
    db.session.delete(answer)
    db.session.commit()


def find():
    return db.session.query(Answer).order_by(Answer.datetime.desc()).all()


def findById(id):
    return Answer.query.get(id)

