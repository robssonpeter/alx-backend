from flask import Flask
import flask

app = Flask(__name__, template_folder="templates/")

@app.route('/')
def home():
    return flask.render_template('0-index.html', name="Jackson")

if __name__ == "__main__":
    app.run()