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


class Item(db.Model):
    __tablename__ = "items"
    item_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    table = db.Column(db.String(1), nullable=False)
    type_ = db.Column(db.String(13), nullable=False)
    rarity = db.Column(db.String(1), nullable=False)
    attuned = db.Column(db.Boolean, nullable=False)
    source = db.Column(db.String(10), nullable=False)
    notes = db.Column(db.String(300))


class Offer(db.Model):
    __tablename__ = "offers"
    offer_id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime)
    status = db.Column(db.String(50))

    # Relationship properties
    sending_user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    sending_user = db.relationship("User", foreign_keys=[sending_user_id])

    receiving_user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    receiving_user = db.relationship("User", foreign_keys=[receiving_user_id])

    offered_item_id = db.Column(db.Integer, db.ForeignKey("items.item_id"))
    offered_item = db.relationship("Item", foreign_keys=[offered_item_id])

    wanted_items = db.relationship("Wanted_Item", back_populates="offer")


class Wanted_Item(db.Model):
    __tablename__ = "wanted_items"
    wanted_item_id = db.Column(db.Integer, primary_key=True)

    # Relationship properties
    offer_id = db.Column(db.Integer, db.ForeignKey("offers.offer_id"))
    offer = db.relationship("Offer", back_populates="wanted_items")

    item_id = db.Column(db.Integer, db.ForeignKey("items.item_id"))
    item = db.relationship("Item")
