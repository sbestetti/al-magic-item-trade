from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/healthz")
def healthz():
    return jsonify(
        {
            "Status": "OK"
        }
    ), 200


if __name__ == "__main__":
    app.run(debug=True)
