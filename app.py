#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from functools import wraps
from flask import Flask, redirect
from flask.globals import request, session
from flask.helpers import url_for
from resources.controllers import loginController, signinController, userController, questionController, \
    answerController
from resources.db.connection import db
from resources.helpers import forum

app = Flask(__name__)

app.secret_key = "my precious"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///forum.db'
db.init_app(app)


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'loggedin' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('login'))

    return wrap


@app.route('/create')
def create():
    forum.create()
    return 'created'


@app.route('/logout')
@login_required
def logout():
    return loginController.logout()


@app.route('/login', methods=['GET', 'POST'])
def login():
    return loginController.login(request)


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    return signinController.signin(request)


@app.route('/')
@login_required
def index():
    return userController.index()


@app.route('/question/<int:id>/answers', methods=['GET', 'POST'])
@login_required
def question_answers(id):
    return questionController.questionAnswers(id, request)


@app.route('/question', methods=['GET', 'POST'])
@login_required
def question():
    return questionController.insert(request)


@app.route('/question/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def question_edit(id):
    return questionController.edit(id, request)


@app.route('/question/delete/<int:id>')
@login_required
def question_remove(id):
    return questionController.delete(id)


@app.route('/answer/question/<int:id>', methods=['GET', 'POST'])
@login_required
def answer_question(id):
    return answerController.insert(id, request)


@app.route('/answer/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def answer_edit(id):
    return answerController.edit(id, request)


@app.route('/answer/delete/<int:id>')
@login_required
def answer_delete(id):
    return answerController.delete(id)


@app.route('/my-questions')
@login_required
def my_questions():
    return questionController.myQuestions()


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print('App rodando em 127.0.0.1:5000')
    app.run(host='127.0.0.1', port=port, debug=True)
