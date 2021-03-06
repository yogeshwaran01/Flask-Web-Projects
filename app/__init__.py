from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from config import Configuartion

app = Flask(__name__)
app.config.from_object(Configuartion)

database = SQLAlchemy(app)
migrate = Migrate(app, database)

login = LoginManager(app)
login.login_view = "auth.login"

from .views import auth
from .views import todo
from .views import tools
from .views import fun
from .views import image
from .views import github
from .views import redirecter


@app.route("/")
def index():
    return render_template("index.html", title="Home")


app.register_blueprint(auth.bp)
app.register_blueprint(todo.bp)
app.register_blueprint(tools.bp)
app.register_blueprint(fun.bp)
app.register_blueprint(image.bp)
app.register_blueprint(github.bp)
app.register_blueprint(redirecter.bp)

from .models.users import User, Todo
from .models.image import Codes
