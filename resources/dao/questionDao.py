from resources.db.connection import db


def insert(question):
    db.session.add(question)
    db.session.commit()


def delete(question):
    db.session.delete(question)
    db.session.commit()

