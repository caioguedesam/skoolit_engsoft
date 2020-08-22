import functools
from skoolit import db
from flask import (
    Blueprint, flash, g, redirect, render_template, request, 
    session, url_for)
from skoolit.usuarios import models 

bp = Blueprint('auth', __name__, url_prefix='/auth')

# @bp.before_app_request
# def load_logged_in_user():
#     user_id = session.get('id_usuario')

#     if user_id is None:
#         g.user = None
#     else:
#         g.user = models.Usuario.query.filter_by(id=user_id).first_or_404()

# Usar quando precisar de que uma view precise de login
# Atualmente não é necessário, já que cada módulo exige login por padrão
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('login.login'))

        return view(**kwargs)
    return wrapped_view