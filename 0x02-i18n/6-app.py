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

users = {
            1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
            2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
            3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
            4: {
                "name": "Teletubby",
                "locale": None,
                "timezone": "Europe/London"
                },
        }


def get_user(user_id=None) -> dict:
    keys = list(users.keys())
    id = int(user_id)
    if user_id is None or id not in keys:
        return None
    elif id in keys:
        return users[id]


@app.before_request
def before_request():
    login_as = request.args.get('login_as')
    user_id = int(login_as) if login_as is not None else None
    user = get_user(user_id)
    flask.g.user = user


@babel.localeselector
def get_locale() -> Union[str, None]:
    user = flask.g.get('user')
    locale = request.args.get('locale', default=None)
    locale_header = request.accept_languages.best_match(Config.LANGUAGES)
    if locale:
        return locale
    elif user and user['locale'] in Config.LANGUAGES:
        return user['locale']
    elif locale_header:
        return locale_header
    else:
        return Config.BABEL_DEFAULT_LOCALE

    """ The function to return the best match of the lang """
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/')
def home() -> str:

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
    current_user = flask.g.get('user')
    if current_user:
        data['logged_in_as'] = users[int(login_as)]
    else:
        data["not_logged_id"] = not_logged_in

    return flask.render_template('6-index.html', **data)


if __name__ == "__main__":
    app.run()
