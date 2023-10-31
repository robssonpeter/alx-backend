#!/usr/bin/env python3
from flask import Flask
import flask
from flask_babel import Babel
from flask import request
from typing import Union

""" The entry file for the web application """


app = Flask(__name__, template_folder="templates/")

class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)

@babel.localeselector
def get_locale() -> Union[str, None]:
    return request.accept_languages.best_match(Config.LANGUAGES)

@app.route('/')
def home() -> str:
    """ The home route for the application """
    return flask.render_template('0-index.html')


if __name__ == "__main__":
    app.run()
