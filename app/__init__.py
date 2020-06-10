from flask import Flask

from .config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from . import models
from . import views
from .my_blueprints import auth, tasks
app.register_blueprint(auth.bp)
app.register_blueprint(tasks.bp)