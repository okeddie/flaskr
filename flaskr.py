#!/bin/python
import sqlite3
from flask import Flask, request,session, g, redirect, url_for, \
     abort, reder_template, flash

# Configuration:
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

# Application Creation:
app = Flask(__name__)
"""From object will look at the given object ( if it's a string it will import it)
and then look for all uppercase variables defined there. in this case the configuration
the config right above"""
app.config.from_object(__name__)
