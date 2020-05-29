from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


inventory = db.Table(
    "inventory",
    db.Column("inventory_id", db.Integer, primary_key=True),
    db.Column(
        "character_id",
        db.Integer,
        db.ForeignKey("character.character_id")),
    db.Column("item_id", db.Integer, db.ForeignKey("item.item_id")),
)


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)
    dci = db.Column(db.String(10), nullable=False, unique=True)
    active = db.Column(db.Boolean, default=True)
    verified = db.Column(db.Boolean, default=False)
    last_login = db.Column(db.DateTime)

    characters = db.relationship('Character', backref='character', lazy=True)


class Character(db.Model):
    character_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey(User.user_id),
        nullable=False)

    user = db.relationship("User", backref=db.backref("user"), lazy=True)
    items = db.relationship("Item", secondary=inventory, lazy="subquery")


class Item(db.Model):
    item_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    type_ = db.Column(db.String(80), nullable=False)
    rarity = db.Column(db.String(30), nullable=False)
    attuned = db.Column(db.Boolean, nullable=False)
    notes = db.Column(db.String(300), nullable=False)
    source = db.Column(db.String(10), nullable=False)

    characters = db.relationship(
        "Character",
        secondary=inventory,
        lazy="subquery")
