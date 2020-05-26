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


# TODO: Remove before prod
@app.route("/create_db")
def create_db():
    try:
        db.create_all()
        return "Done", 200
    except Exception as e:
        return f"Error creating DB: {e}", 500


if __name__ == "__main__":
    app.run(debug=True)
