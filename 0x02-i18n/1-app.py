#!/usr/bin/env python3
from flask import Flask
import flask
from flask_babel import Babel
""" The entry file for the web application """


app = Flask(__name__, template_folder="templates/")
babel = Babel(app)


class Config:
    LANGUAGES = ["en", "fr"]

    def __init__(self, locale = "en", timezone="UTC") -> None:
        babel.default_locale = locale
        babel.default_timezone = timezone

config = Config()

@app.route('/')
def home() -> str:
    """ The home route for the application """
    return flask.render_template('0-index.html')


if __name__ == "__main__":
    app.run()
