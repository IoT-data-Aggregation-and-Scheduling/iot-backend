from flask import Flask, redirect, url_for
import os

def create_app(config):
    app = Flask(__name__)

    if config['env'] != 'local':
        app.debug = False
        app.testing = False
    else:
        app.debug = True
        app.testing = True

    from .api import mainApp
    app.register_blueprint(mainApp, url_prefix='/')

    # Add a default root route.
    @app.route("/")
    def index():
        print('This is standard output')
        return redirect(url_for('mainApp.index'))
    return app

    @app.route('/<path:dummy>')
    def fallback(dummy):
        return redirect(url_for('mainApp.index'))