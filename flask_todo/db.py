import psycopg2

import click

from flask import current_app, g
from flask.cli import with_appcontext

#   1.  import module in db.py
#   2.  set up connection in get_db
#           -  server?
#           -  database name?
#           -  user?
#   3.  handle closing connections in close_db
#   4.  setup init_db function to clear out and create tables, w/ cli command
#   5. register w/ app

##############################################################

def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect("dbname='todo_manager' user='csetuser' host='127.0.0.1'")

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        cur = db.cursor()
        cur.execute(f.read())
        db.commit()
        db.close()

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
