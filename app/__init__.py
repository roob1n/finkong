import os

from flask import (Flask, render_template)

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'finkong.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from app.filters import format_currency
    # Register the filter with Flask
    app.jinja_env.filters['format_currency'] = format_currency

    # Set up the database handler
    from . import db
    db.init_app(app)

    # Set up the auth blueprint
    from . import auth
    app.register_blueprint(auth.bp)

    # Set up the account blueprint
    from . import account
    app.register_blueprint(account.bp)

    # Set up the category blueprint
    from . import category
    app.register_blueprint(category.bp)

    # a simple page that says hello
    @app.route('/')
    def index():
        return render_template('index.html')

    return app