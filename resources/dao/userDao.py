from resources.db.connection import db
from resources.models.user import User


def insert(user):
    db.session.add(user)
    db.session.commit()


def delete(user):
    db.session.delete(user)
    db.sesssion.commit()


def findByLogin(username, password):
    return db.session.query(User).filter(User.username==username, password==password).first()


def findById(id):
    return db.session.query(User).get(id)


def findByUsername(username):
    return db.session.query(User).filter(User.username==username).first()

