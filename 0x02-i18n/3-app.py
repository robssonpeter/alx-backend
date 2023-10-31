#!/usr/bin/env python3
from flask import Flask
import flask
from flask_babel import Babel, gettext
from flask import request
from typing import Union
import jinja2

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
    return 'fr'
    """ The function to return the best match of the lang """
    return request.accept_languages.best_match(Config.LANGUAGES)

@app.route('/')
def home() -> str:
    """ The home route for the application """
    home_title = gettext('home_title')
    home_header = gettext('home_header')
    data = {
        "home_header": home_header,
        "home_title": home_title,
    }

    return flask.render_template('3-index.html', **data)


if __name__ == "__main__":
    app.run()
