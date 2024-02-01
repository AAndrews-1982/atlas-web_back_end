#!/usr/bin/env python3
"""3-app.y file"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """Configuration class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """function to get user locale"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def gettext():
    """get text function"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """initial route to index"""
    # from flask_babel import gettext as _
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(debug=True)
