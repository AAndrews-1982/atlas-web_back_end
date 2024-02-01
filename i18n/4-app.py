#!/usr/bin/env python3
"""A simple Flask application that
supports internationalization."""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    Configuration class to set up languages and timezone.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Initialize the Flask application
app = Flask(__name__)
# Load the configuration from the `Config` class
app.config.from_object(Config)
# Initialize Babel with the app for internationalization support
babel = Babel(app)


def get_locale():
    """
    Select a language translation for a request based on
    the request's parameters or headers.
    """
    # Attempt to get the locale from the URL parameters
    force_locale = request.args.get('locale')
    if force_locale and force_locale in app.config['LANGUAGES']:
        return force_locale
    # Fallback to the best match from the accepted languages in the request
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    The index route that renders the main page.

    Returns:
        A rendered template of '4-index.html'.
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    # Run the app in debug mode for development purposes
    app.run(debug=True)
