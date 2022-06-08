from flask import redirect, current_app as app, request, jsonify
from .config import *
from pprint import pprint

# Setting up secret key
app.secret_key = SECRET_KEY

"""

Routes: /emotionalysis


"""


@app.route("/<string:text>")
@app.route("/emotionalysis/<string:text>")
def analayze(text: str):
    resp = {
        "text": text,
        "emotion": [
            {"happy": 70},
            {"sad": 50}
        ]
    }

    return jsonify(resp)
