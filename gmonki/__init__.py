# -*- coding: utf-8 -*-
from flask import Flask, request
from flask.ext.babel import Babel
from flask.ext.mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.user import login_required, SQLAlchemyAdapter, UserManager, UserMixin
from flask.ext.user import roles_required
from werkzeug.routing import Rule

import os

def create_app(test_config=None):                   # For automated tests
    # Setup Flask and acquire configuration
    app = Flask(__name__)
    gmonki_config = 'config.' + os.environ['GMONKI_CONFIG']
    app.config.from_object(gmonki_config)

    # Load local_settings.py if file exists         # For automated tests
    try: app.config.from_object('local_settings')
    except: pass

    # Over-write app config                         # For automated tests
    if test_config:
        for key, value in test_config.items():
            app.config[key] = value

    # Setup Flask-Mail, Flask-Babel and Flask-SQLAlchemy
    app.mail = Mail(app)
    app.babel = babel = Babel(app)
    app.db = db = SQLAlchemy(app)

    @babel.localeselector
    def get_locale():
        return request.accept_languages.best_match(['en', 'nl'])

    # Define the User-Roles pivot table
    user_roles = db.Table('user_roles',
        db.Column('id', db.Integer(), primary_key=True),
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id', ondelete='CASCADE')))

    # Define Role model
    class Role(db.Model):
        id = db.Column(db.Integer(), primary_key=True)
        name = db.Column(db.String(50), unique=True)

    # Define User model. Make sure to add flask.ext.user UserMixin!!
    class User(db.Model, UserMixin):
        id = db.Column(db.Integer, primary_key=True)
        active = db.Column(db.Boolean(), nullable=False, default=False)
        username = db.Column(db.String(50), nullable=True, unique=True)
        email = db.Column(db.String(255), nullable=True, unique=True)
        email_confirmed_at = db.Column(db.DateTime())
        password = db.Column(db.String(255), nullable=False, default='')
        reset_password_token = db.Column(db.String(100), nullable=False, default='')
        # Relationships
        roles = db.relationship('Role', secondary=user_roles,
                backref=db.backref('users', lazy='dynamic'))
    app.User = User

    # Reset all the database tables
    db.create_all()

    # Make some 'play' roles for testing
    secret_role = Role(name='secret')
    agent_role = Role(name='agent')
    admin_role = Role(name='admin')

    # Setup Flask-User
    db_adapter = SQLAlchemyAdapter(db,  User)
    user_manager = UserManager(db_adapter, app)

    # Create 'user007' user with 'secret' and 'agent' roles
    if not User.query.filter(User.username=='user007').first():
        user1 = User(username='user007', email='007@marktward.name', active=True,
                password=user_manager.password_crypt_context.encrypt('Password1'))
        user1.roles.append(secret_role)
        user1.roles.append(agent_role)
        db.session.add(user1)

    if not User.query.filter(User.username=='Queue').first():
        user2 = User(username='Queue', email='Q@marktward.name', active=True,
                password=user_manager.password_crypt_context.encrypt('Password1'))
        user2.roles.append(secret_role)
        user2.roles.append(agent_role)
        user2.roles.append(admin_role)
        db.session.add(user2)

    # commit all db entries
    db.session.commit()

    return app

app = create_app()

# routing rules
app.url_map.add(Rule('/index', endpoint='index'))

# views
from gmonki.views import standard
from gmonki.views import admin
