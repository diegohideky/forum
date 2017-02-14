from flask.globals import session
from flask.helpers import url_for
from flask.templating import render_template
from werkzeug.utils import redirect
from resources.dao import questionDao, userDao
from resources.models.question import Question


def insert(request):
    if request.method == 'POST':
        questionDao.insert(Question(request.form['pergunta'], session['userId']))
    return redirect(url_for('index'))


def questionAnswers(id, request):
    if request.method == 'POST':
        questionDao.insert(Question(request.form['pergunta'], session['userId']))
    question = questionDao.findById(id)
    user = userDao.findById(session['userId'])
    return render_template('pages/question.html', question=question, user=user)

