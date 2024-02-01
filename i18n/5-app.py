#!/usr/bin/env python3
"""4-app.y file"""
from flask import Flask, render_template, request, g
from flask_babel import Babel

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Configuration class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


# @babel.localeselector
def get_locale():
    """function to get user locale"""
    force_locale = request.args.get('locale')
    if force_locale and force_locale in app.config['LANGUAGES']:
        return force_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """Get user function"""
    user_id = int(request.args.get('login_as'))
    if user_id in users:
        return user_id
    else:
        return None


@app.before_request
def before_request():
    """Before request function"""
    g.user = get_user()


@app.route('/')
def index():
    """initial route to index"""
    # from flask_babel import gettext as _
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
