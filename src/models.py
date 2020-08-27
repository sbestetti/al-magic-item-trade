from werkzeug.security import generate_password_hash, check_password_hash

from dao import db


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
    password = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean, default=True)
    verified = db.Column(db.Boolean, default=False)
    last_login = db.Column(db.DateTime)
    authenticated = db.Column(db.Boolean, default=False)

    characters = db.relationship('Character', backref='character', lazy=True)

    def __repr__(self):
        return f"<USER> {self.user_id}: {self.email}"

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def is_active(self):
        return self.active

    def get_id(self):
        return self.email

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False


class Character(db.Model):
    character_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    race = db.Column(db.String(80), nullable=False)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey(User.user_id),
        nullable=False)

    user = db.relationship("User", backref=db.backref("user"), lazy=True)
    items = db.relationship("Item", secondary=inventory, lazy="subquery")
    levels = db.relationship("Level", backref=db.backref("character"))

    def __repr__(self):
        return f"<CHARACTER> {self.character_id}: {self.name}"


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

    def __repr__(self):
        return f"<ITEM_CLASS> {self.item_id}: {self.name}"


class Offer(db.Model):
    offer_id = db.Column(db.Integer, primary_key=True)

    offered_item = db.Column(
        db.Integer,
        db.ForeignKey(Item.item_id),
        nullable=False)

    wanted_item = db.Column(
        db.Integer,
        db.ForeignKey(Item.item_id),
        nullable=False)

    date_created = db.Column(db.DateTime)
    accepted = db.Column(db.Boolean)

    def __repr__(self):
        return f"<OFFER> {self.offer_id}"


class Level(db.Model):
    level_id = db.Column(db.Integer, primary_key=True)
    class_ = db.Column(db.String(80), nullable=False)
    levels = db.Column(db.Integer, nullable=False)

    character_id = db.Column(
        db.Integer,
        db.ForeignKey(Character.character_id),
        nullable=False)
