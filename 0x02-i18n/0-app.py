#!/usr/bin/env python3
from flask import Flask
import flask
""" The entry file for the web application """


app = Flask(__name__, template_folder="templates/")

@app.route('/')
def home() -> str:
    """ The home route for the application """
    return flask.render_template('0-index.html')


if __name__ == "__main__":
    app.run()
