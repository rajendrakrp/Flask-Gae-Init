from functools import wraps
from flask import redirect, request
from google.appengine.api import users

def login_required(f):

    @wraps(f)
    def decorated_view(*args, **kwargs):
        if users.get_current_user() is None:
            return redirect(users.create_login_url(dest_url=request.url))
        return f(*args, **kwargs)
    return decorated_view

