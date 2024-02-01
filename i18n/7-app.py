#!/usr/bin/env python3
"""Babel locale from request"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz

app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": "None", "timezone": "Europe/Spain"},
    42: {"name": "Boy", "locale": "fr", "timezone": "Europe/Paris"},
}


class Config():
    """Class to configure language"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object('7-app.Config')


# @babel.localselector
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
babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def my_home():
    """Method template that simply outputs a message"""
    return render_template('./7-index.html')


def get_user():
    """function that returns a user dictionary"""
    user = request.args.get('login_as')
    if user:
        return users[int(user)]
    else:
        return None


@app.before_request
def before_request():
    """use get_user to find a user if any,
    and set it as a global on flask.g.user
    """
    g.user = get_user()


@babel.timezoneselect
def get_timezone():
    """Function to get a timezone"""
    # 1. Timezone from URL parameters
    if request.args.get('timezone'):
        u_timezone = request.args.get('timezone')
        try:
            pytz.timezone(u_timezone)
            return u_timezone
        except pytz.UnknownTimeZoneError:
            pass
    # 2.  Time zone from user settings
    if g.user and g.user.get('timezone'):
        u_timezone = g.user.get('timezone')
        try:
            pytz.timezone(u_timezone)
            return u_timezone
        except pytz.UnknownTimeZoneError:
            pass
    # 3. Default to UTC
    return 'UTC'


# babel.init_app(app, locale_selector=get_locale)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
