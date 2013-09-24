from flaskext import wtf

class TestForm(wtf.Form):
    name = wtf.TextField("Name")
