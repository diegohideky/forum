from resources.db.connection import db


def insert(answer):
    db.session.add(answer)
    db.session.commit()


def delete(answer):
    db.session.delete(answer)
    db.session.commit()

