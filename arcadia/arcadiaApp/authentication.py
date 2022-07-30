from flask import redirect, session, url_for
from functools import wraps

def ensurelogin(params):
    @wraps(params)
    def wrap(*args, **kwargs):
        if not bool(session.get('UserID', False)):
            return redirect(url_for('app_bp.login'))
        return params(*args, **kwargs)
    return wrap