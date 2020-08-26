from flask_login import LoginManager

from models import User

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_email):
    return User.query.filter_by(email=user_email).first()
