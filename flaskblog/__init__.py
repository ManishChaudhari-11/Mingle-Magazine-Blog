import json

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_ckeditor import CKEditor
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

with open("flaskblog/config.json", "r") as f:
    params = json.load(f)["params"]

app = Flask(__name__)
app.config["SECRET_KEY"] = params["super-secret-key"]
app.config["SQLALCHEMY_DATABASE_URI"] = params["local_db_uri"]
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "users.login"
login_manager.login_message_category = "info"

app.config["CKEDITOR_PKG_TYPE"] = "full-all"
ckeditor = CKEditor(app)

app.config.update(
    MAIL_SERVER="smtp.gmail.com",
    MAIL_PORT="465",
    MAIL_USE_SSL=True,
    MAIL_USERNAME=params["gmail-user"],
    MAIL_PASSWORD=params["gmail-pass"],
)
mail = Mail(app)

from flaskblog.errors.handlers import errors
from flaskblog.main.routes import main
from flaskblog.posts.routes import posts
from flaskblog.users.routes import users

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)
app.register_blueprint(errors)
