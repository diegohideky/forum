from flask.globals import session
from flask.helpers import url_for
from flask.templating import render_template
from werkzeug.utils import redirect
from resources.dao import answerDao, userDao, questionDao
from resources.models.answer import Answer


def insert(id, request):
    if request.method == 'POST':
        answerDao.insert(Answer(request.form['resposta'], session['userId'], id))
    return redirect(url_for('question_answers', id=id))


def edit(id, request):
    answer = answerDao.findById(id)
    if request.method == 'POST':
        answer.text = request.form['resposta']
        answerDao.insert(answer)
        return redirect(url_for('question_answers', id=answer.question_id))
    question = questionDao.findById(answer.question_id)
    user = userDao.findById(session['userId'])
    return render_template('pages/question.html', answer=answer, question=question, user=user, editAnswer=True)


def delete(id):
    answer = answerDao.findById(id)
    answerDao.delete(answer)
    return redirect(url_for('question_answers', id=answer.question_id))