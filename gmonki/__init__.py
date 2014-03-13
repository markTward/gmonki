# -*- coding: utf-8 -*-
from flask import Flask, request
from flask_sslify import SSLify
from flask.ext.babel import Babel
from flask.ext.mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.user import login_required, SQLAlchemyAdapter, UserManager, UserMixin
from flask.ext.user import roles_required
from werkzeug.routing import Rule

import os

# Setup Flask and acquire configuration
app = Flask(__name__)
gmonki_config = 'config.' + os.environ['GMONKI_CONFIG']
app.config.from_object(gmonki_config)

app.mail = Mail(app)
app.babel = babel = Babel(app)
db = SQLAlchemy(app)

# extend app with Flask-SSLify, forcing https per config setting
if app.config['USE_SSLIFY']:
    sslify = SSLify(app)

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en', 'nl'])

#flask_user
from models.userrole import User, Role
app.User = User
app.Role = Role

# Setup Flask-User
db_adapter = SQLAlchemyAdapter(db,  User)
user_manager = UserManager(db_adapter, app)

# routing rules
app.url_map.add(Rule('/index', endpoint='index'))

# views
from gmonki.views import standard
from gmonki.views import admin
