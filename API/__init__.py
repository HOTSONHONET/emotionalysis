from warnings import filterwarnings
from flask import Flask


# Filtering out all warnings
filterwarnings("ignore")


# A display at the start of the app
print("[INFO] Keep calm and Enjoy the drill")


def start_app():
    app = Flask(__name__, instance_relative_config=False)
    with app.app_context():
        from . import routes
        return app
