#!/usr/bin/env python3
"""Babel locale from request"""
from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": "None", "timezone": "Europe/Londo"},
}


class Config():
    """Class to configure language"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object('6-app.Config')


@babel.localeselector
def get_locale():
    """Determine the best match with our supported languages."""
    # 1. Locale from URL parameters
    if request.args.get('locale'):
        user_locale = request.args.get('locale')
        if user_locale in app.config['LANGUAGES']:
            return user_locale

        # 2. Locale from user settings
    elif g.user and g.user.get('locale')\
            and g.user['locale'] in app.config['LANGUAGES']:
        return g.user.get('locale')
    else:
        # 3. Locale from request header
        return request.accept_languages.best_match(app.config['LANGUAGES'])


# Set up Babel to work with the Flask application
# babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def my_home():
    """Method template that simply outputs a message"""
    return render_template('./6-index.html')


def get_user():
    """function that returns a user dictionary"""
    if request.args.get('login_as'):
        user_id = int(request.args.get('login_as'))
        if user_id in users:
            print(user_id)
            return users.get(user_id)
    else:
        return None


@app.before_request
def before_request():
    """use get_user to find a user if any,
    and set it as a global on flask.g.user
    """
    g.user = get_user()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
