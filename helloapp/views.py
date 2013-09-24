from flask import request, render_template, g
from google.appengine.api import users
from forms import TestForm
from decorators import login_required
from helloapp import app

@app.before_request
def lookup_current_user():
    g.user = users.get_current_user()

@login_required
def home():

    form = TestForm()
    if form.validate_on_submit():
        name = form.name.data
        return render_template('home.html', form=form, name=name)
    return render_template('home.html', form=form, logout=users.create_logout_url(request.url))
    
