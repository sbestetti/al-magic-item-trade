from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)
    dci = db.Column(db.String(10), nullable=False, unique=True)
    active = db.Column(db.Boolean, default=True)
    verified = db.Column(db.Boolean, default=False)
    last_login = db.Column(db.DateTime)

    characters = db.relationship('Character', backref='user', lazy=True)


class Character(db.Model):
    character_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey(User.user_id),
        nullable=False
        )

    user = db.relationship("User", backref=db.backref("user"), lazy=True)


class Item(db.Model):
    item_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    type_ = db.Column(db.String(80), nullable=False)
    rarity = db.Column(db.String(30), nullable=False)
    attuned = db.Column(db.Boolean, nullable=False)
    notes = db.Column(db.String(300), nullable=False)
    source = db.Column(db.String(10), nullable=False)
