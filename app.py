#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from functools import wraps
from flask import Flask, redirect
from flask.globals import request, session
from flask.helpers import url_for
from flask.templating import render_template
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


@app.route('/')
@login_required
def index():
  return render_template('pages/index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
  return render_template('pages/login.html')


@app.route('/create')
def create():
  forum.create()
  return 'created'


if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='127.0.0.1', port=port, debug=True)

