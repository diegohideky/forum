from flask.globals import session
from flask.helpers import url_for
from flask.templating import render_template
from werkzeug.utils import redirect
from resources.dao import userDao
from resources.helpers import encrypt


def login(request):
    if request.method == 'POST':
        user = userDao.findByLogin(request.form['usuario'], encrypt.encode(request.form['senha']))
        if user:
            session['loggedin'] = True
            session['userId'] = user.id
            return redirect(url_for('index'))
    return render_template('pages/login.html')


def logout():
    session.pop('loggedin')
    session.pop('userId')
    return redirect(url_for('login'))

