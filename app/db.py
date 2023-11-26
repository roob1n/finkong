import sqlite3

import click
from flask import current_app, g

# Initialise the database based on the schema.sql file
def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

# Seed the db with the initial values
def seed_init_db():
    db = get_db()

    with current_app.open_resource('seed-init.sql') as f:
        db.executescript(f.read().decode('utf8'))

# Seed the db with the test data
def seed_test_db():
    db = get_db()

    with current_app.open_resource('seed-testdata.sql') as f:
        db.executescript(f.read().decode('utf8'))

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    seed_init_db()
    click.echo('Initialized the database and seeded with init values.')

@click.command('seed-test')
def seed_test_db_command():
    seed_test_db()
    click.echo('Seeded the database with test data.')

# add the close_db function and the init_db_command to the app context
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    app.cli.add_command(seed_test_db_command)