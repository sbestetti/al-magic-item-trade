from flask import Flask, jsonify

from models import db

app = Flask(__name__)
app.config.from_pyfile("./settings.py")

db.init_app(app)


@app.route("/healthz")
def healthz():
    return jsonify({
        "Status": "OK"
    }), 200


@app.route("/run_tests")
def run_tests():
    # TODO: Move when tests setup
    # Tests
    try:
        db.drop_all()
        db.create_all()
    except Exception as e:
        return f"Error creating DB: {e}", 500
    from datetime import datetime

    from models import User, Character, Item

    new_user_1 = User(
        name="Sergio",
        email="sergio@email.com",
        dci="12345678",
        active=True,
        verified=False,
        last_login=datetime.now()
        )

    new_user_2 = User(
        name="Rosca",
        email="rosca@email.com",
        dci="910111213",
        active=True,
        verified=False,
        last_login=datetime.now()
        )

    new_character_1 = Character(
        name="Tinemir",
        )

    new_character_2 = Character(
        name="Uther",
    )

    new_character_3 = Character(
        name="Rosquette",
    )

    new_item_1 = Item(
        name="Magic Sword",
        type_="Weapon",
        rarity="Unique",
        attuned=True,
        notes="Bleeds",
        source="DMG"
    )

    new_item_2 = Item(
        name="Magic Staff",
        type_="Weapon",
        rarity="Rare",
        attuned=True,
        notes="Bleeds",
        source="DMG"
    )

    new_item_3 = Item(
        name="Magic beads",
        type_="Weapon",
        rarity="Uncommon",
        attuned=True,
        notes="Bleeds",
        source="DMG"
    )

    new_character_1.items.append(new_item_1)
    new_character_1.items.append(new_item_2)

    new_character_3.items.append(new_item_3)

    new_user_1.characters.append(new_character_1)
    new_user_1.characters.append(new_character_2)
    new_user_2.characters.append(new_character_3)

    db.session.add(new_user_1)
    db.session.add(new_user_2)

    db.session.commit()

    # Query tests
    my_chars = Character.query.filter_by(user=new_user_1)
    items = list()
    for char in my_chars:
        for item in char.items:
            items.append(item.name)
    print(items)

    return "Finished", 200


if __name__ == "__main__":
    app.run(debug=True)
