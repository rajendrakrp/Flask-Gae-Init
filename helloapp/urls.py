import views
from helloapp import app

app.add_url_rule('/', view_func=views.home, methods=['GET', 'POST'])
