import time
import datetime
import psycopg2

from flask import Flask, request,  make_response, render_template
from flask import current_app, g
from flask.cli import with_appcontext

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DB_NAME='todo_manager',
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    from . import db
    db.init_app(app)

#########################################

# List all tasks

    @app.route('/', methods=['GET', 'POST'])
    def index():
        task = []

        if request.method == 'POST':
            item = request.form['item']

            if item:
                con = db.get_db()
                cur = conn.cursor()
                cur.execute("SELECT * FROM task_list;")
                cur.fetchone()

            cur.close()
            conn.close()

        return render_template('index.html')

#########################################

#   Create a task

    @app.route('/create', methods=['GET', 'POST'])
    def add_task():
        if request.method == 'POST':
            item = request.form['item']

            if item:
                conn = psycopg2.connect("dbname='todo_manager' user='csetuser' host=127.0.0.1")

                con = db.get_db()
                cur = conn.cursor()
                cur.execute("INSERT INTO task_list (task, timestamp_of_task, completed) VALUES (%s, %s, %s)", {{ request.form['item'] }})

            ts = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            conn.commit()

            cur.close()
            conn.close()

            if not item:
                return 'Error'

            return render_template('create.html', ts=ts, item=item)


        return render_template('create.html')


    return app
