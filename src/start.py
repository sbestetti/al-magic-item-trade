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

    try:
        db.create_all()
    except Exception as e:
        return f"Error creating DB: {e}", 500
    from datetime import datetime
    from models import User, Character

    new_user = User(
        name="Sergio",
        email="sergio@email.com",
        dci="12345678",
        active=True,
        verified=False,
        last_login=datetime.now()
        )

    new_character_1 = Character(
        name="Tinemir",
        user=new_user
        )

    new_character_2 = Character(
        name="Uther",
    )

    new_user.characters.append(new_character_2)

    db.session.add(new_user)
    db.session.add(new_character_1)
    db.session.commit()

    # Query tests
    my_chars = Character.query.filter_by(user=new_user).all()
    for char in my_chars:
        print(char.name)

    return "Finished", 200


if __name__ == "__main__":
    app.run(debug=True)
