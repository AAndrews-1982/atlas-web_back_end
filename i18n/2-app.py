#!/usr/bin/env python3

""" A simple Flask application with Babel integration
for i18n and l10n """

from flask import Flask, request
from flask_babel import Babel


# Configuration class
class Config:
    """ Configuration for the Flask app """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Initialize Flask application
web_app = Flask(__name__)

# Apply configuration from Config class
web_app.config.from_object(Config)

# Initialize Babel with the Flask app
babel = Babel(web_app)


@babel.localeselector
def get_locale():
    """ Determine the best match with our supported languages. """
    return request.accept_languages.best_match(
        web_app.config['LANGUAGES'])


@web_app.route('/')
def home_page():
    """ Render the home page template """
    # Your routing and view logic here


if __name__ == "__main__":
    web_app.run(debug=True)
