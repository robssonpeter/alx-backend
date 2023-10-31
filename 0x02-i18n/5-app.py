#!/usr/bin/env python3
""" The entry file for the web application """
from flask import Flask
import flask
from flask_babel import Babel, gettext
from flask import request
from typing import Union


app = Flask(__name__, template_folder="templates/")


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> Union[str, None]:
    locale = request.args.get('locale', default=None)
    if locale:
        return locale
    """ The function to return the best match of the lang """
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/')
def home() -> str:
    users = {
        1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
        2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
        3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
        4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
    }
    """ The home route for the application """
    home_title = gettext('home_title')
    home_header = gettext('home_header')
    logged_in_as = gettext('logged_in_as')
    not_logged_in = gettext('not_logged_in')
    data = {
        "home_header": home_header,
        "home_title": home_title,
    }
    login_as = request.args.get('login_as')
    keys = list(users.keys())
    if login_as and int(login_as) in keys:
        data['logged_in_as'] = users[int(login_as)]
    else:
        data["not_logged_id"] = not_logged_in

    return flask.render_template('5-index.html', **data)


if __name__ == "__main__":
    app.run()
