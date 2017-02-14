from flask.globals import session
from flask.helpers import url_for
from werkzeug.utils import redirect
from resources.dao import answerDao
from resources.models.answer import Answer


def insert(id, request):
    if request.method == 'POST':
        answerDao.insert(Answer(request.form['resposta'], session['userId'], id))
    return redirect(url_for('question_answers', id=id))
