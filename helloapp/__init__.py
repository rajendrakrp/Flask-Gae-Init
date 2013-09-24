import fix_path
import settings
from flask import Flask

app = Flask('helloapp')
app.config.from_object(settings)

import views
import urls
