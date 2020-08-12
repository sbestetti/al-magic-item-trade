from flask import Flask

from views import index, register


def get_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "secret"

    app.register_blueprint(index.bp)
    app.register_blueprint(register.bp)

    @app.route("/healthz")
    def healthz():
        return "OK", 200

    return app
