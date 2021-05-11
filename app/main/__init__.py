from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

app.config["SECRET_KEY"]= '5cd29fc8372646c71ece42e8'
app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///data.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS "] = True


from main import route
