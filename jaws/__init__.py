
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from jaws.database import db_session
from jaws.posts import posts

# configuration
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)
app.register_blueprint(posts)


@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()
