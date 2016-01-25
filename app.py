#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os

from routes import routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

app.register_blueprint(routes)

db = SQLAlchemy(app)

if __name__ == '__main__':
    app.debug = True
    app.run()
