from flask.globals import session
from flask.helpers import url_for
from werkzeug.utils import redirect
from resources.dao import userDao
from resources.helpers import encrypt
from resources.models.user import User


def signin(request):
    if request.method == 'POST':
        if request.form['senha'] == request.form['senharepete']:
            userDao.insert(User(request.form['usuario'], encrypt.encode(request.form['senha']), request.form['tipo']))
            user = userDao.findByUsername(request.form['usuario'])
            session['loggedin'] = True
            session['userId'] = user.id
        return redirect(url_for('index'))
    return redirect(url_for('login'))