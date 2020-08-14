import functools
from skoolit import db
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = db.execute("SELECT * FROM user WHERE id = :id",
                        {"id": user_id}).fetchone()
        db.close() 


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('login'))

        return view(**kwargs)
    return wrapped_view