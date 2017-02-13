from resources.db.connection import db


def insert(user):
    db.session.add(user)
    db.session.commit()


def delete(user):
    db.session.delete(user)
    db.session.commit()

