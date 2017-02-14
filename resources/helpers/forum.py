#!/usr/bin/env python
# -*- coding: utf-8 -*-
from resources.db.connection import db
from resources.helpers import encrypt
from resources.models.answer import Answer
from resources.models.question import Question
from resources.models.user import User


def create():
    #create the database and the db tables
    db.create_all()

    db.session.add(User('test', encrypt.encode('123123'), 'Estudante'))
    db.session.add(Question('question 1', 1))
    db.session.add(Answer('answer 1', 1, 1))
    db.session.commit()

