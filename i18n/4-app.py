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


app.config.from_object('4-app.Config')


@babel.localeselector
def get_locale():
    """
    Determine the best matching language from supported languages.
    """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        # Return the locale if it's explicitly specified in the request.
        return locale
    # Otherwise, return the best match from the Accept-Language header.
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def my_home():
    """
    Render the home page of the application.
    """
    return render_template('./4-index.html')


if __name__ == "__main__":
    # This configuration makes the application accessible over the network.
    app.run(host="0.0.0.0", port="5000")
