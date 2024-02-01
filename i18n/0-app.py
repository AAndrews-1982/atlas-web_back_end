#!/usr/bin/env python3

""" A simple Flask application """

from flask import Flask, render_template

# Initialize Flask application
web_app = Flask(__name__)

# Define the route for the root URL
@web_app.route('/')
def home_page():
    """ Render the home page template """
    return render_template('home.html')

# Run the application
if __name__ == "__main__":
    web_app.run()
