from main import app
from flask_sqlalchemy import SQLAlchemy
from main import login_manager
from flask_login import UserMixin
db = SQLAlchemy(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), nullable=False, unique= True )
    email = db.Column(db.String(120), nullable=False, unique=True)
    password= db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'User({self.username}, {self.email})'