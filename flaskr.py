#!/bin/python
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing

# Configuration:
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

#The variables above have been set into Flask.

# Application Creation:
app = Flask(__name__)
"""from_object() will look at the given object ( if it's a string it will import it)
and then look for all uppercase variables defined in it. in this case the configuration
the config right above"""	
app.config.from_object(__name__)

# Connection to database
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])
# Initialize sqlite database
def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

init_db()

# Start App. We use port 80 and must not use quotes on it.
if __name__ == '__main__':
    app.run(host='0.0.0.0')
