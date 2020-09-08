from werkzeug.security import generate_password_hash, check_password_hash

from dao import db


class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)
    dci = db.Column(db.String(10), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean, default=True)
    verified = db.Column(db.Boolean, default=False)
    last_login = db.Column(db.DateTime)
    authenticated = db.Column(db.Boolean, default=False)

    # Relationship properties
    items = db.relationship("Item", back_populates="user")

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


class Item_Model(db.Model):
    __tablename__ = "item_models"
    item_model_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    type_ = db.Column(db.String(80), nullable=False)
    rarity = db.Column(db.String(30), nullable=False)
    attuned = db.Column(db.Boolean, nullable=False)
    notes = db.Column(db.String(300), nullable=False)
    source = db.Column(db.String(10), nullable=False)

    # Items mapping
    items = db.relationship("Item", back_populates="item_model")

    def __repr__(self):
        return f"<ITEM_CLASS> {self.item_model_id}: {self.name}"


class Item(db.Model):
    __tablename__ = "items"
    item_id = db.Column(db.Integer, primary_key=True)
    character = db.Column(db.String(80))

    # User mapping
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    user = db.relationship("User", back_populates="items")

    # Item mapping
    item_model_id = db.Column(
        db.Integer,
        db.ForeignKey('item_models.item_model_id')
        )
    item_model = db.relationship("Item_Model", back_populates="items")

    def __repr__(self):
        return f"<ITEM> {self.item_id}"


class Offer(db.Model):
    offer_id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime)
    status = db.Column(db.String(50))

    # Relationship properties
    offered_item = db.Column(
        db.Integer,
        db.ForeignKey(Item.item_id),
        nullable=False)

    wanted_item = db.Column(
        db.Integer,
        db.ForeignKey(Item.item_id),
        nullable=False)

    def __repr__(self):
        return f"<OFFER> {self.offer_id}"
