from flask import Flask, jsonify

from models import db


def get_app():
    app = Flask(__name__)
    app.config.from_pyfile("./settings.py")

    db.init_app(app)

    @app.route("/healthz")
    def healthz():
        return jsonify({
            "Status": "OK"
        }), 200

    return app
