"""Script containing a basic flask app
   and a basic babel set up
"""

from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """flask configurations for babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def hello_world():
    """Method that renders a template"""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
