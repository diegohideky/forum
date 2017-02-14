from flask.globals import session
from flask.templating import render_template
from resources.dao import userDao, questionDao


def index():
    user = userDao.findById(session['userId'])
    questions = questionDao.find()
    return render_template('pages/questions.html', user=user, questions=questions)