from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.exc import IntegrityError

db = SQLAlchemy()


def add_user(user):
    user.password = generate_password_hash(user.password)
    try:
        db.session.add(user)
        db.session.commit()
    except IntegrityError:
        raise
    return None
