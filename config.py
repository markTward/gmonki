# -*- coding: utf-8 -*-
"""
    config.py
"""
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # Environment Settings
    DEBUG = False
    TESTING = False

	# Flask App
    SECRET_KEY = 'THIS IS AN INSECURE SECRET' 

    CSRF_ENABLED = True
    USE_SSLIFY = False

    # Configure Flask-User
    USER_ENABLE_USERNAME        = True              # Register and Login with username
    USER_ENABLE_EMAIL           = True              # Register with email
    USER_ENABLE_CONFIRM_EMAIL   = True              # Require email confirmation
    USER_ENABLE_CHANGE_USERNAME = True
    USER_ENABLE_CHANGE_PASSWORD = True
    USER_ENABLE_FORGOT_PASSWORD = True

    # RESTful API settings
    API_VERSION_CURRENT = '1'
    API_VERSION_ACTIVE = ['1']
    API_VERSION_DEPRECATED = []

    #HTTP Headers
    DEFAULT_LANGUAGE = 'en'
    
class ConfigDev(Config):
    # Flask App
    DEBUG = True
    TRAP_BAD_REQUEST_ERRORS = True
    USE_SSLIFY = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db/gmonki.db') 

    # Configure Flask-Mail
    MAIL_SERVER   = 'smtp.gmail.com'
    MAIL_PORT     = 465
    MAIL_USE_SSL  = True
    MAIL_USERNAME = os.environ.get('GMAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('GMAIL_PASSWD')
    MAIL_DEFAULT_SENDER = '"Sender" <noreply@gmonki.com>'

class ConfigStg(Config):
    #USE_SSLIFY = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
	
    # Configure Flask-Mail
    MAIL_SERVER   = 'smtp.mandrillapp.com'
    MAIL_PORT     = 465
    MAIL_USE_SSL  = True
    MAIL_USERNAME = os.environ.get('MANDRILL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MANDRILL_APIKEY')
    MAIL_DEFAULT_SENDER = '"Sender" <noreply@gmonki.com>'

class ConfigTest(Config):
    TESTING = True
    
# eclipse    
class ConfigPyDev(ConfigDev):
    DEBUG_WITH_APTANA = True

# heroku foreman 
class ConfigDevFm(ConfigDev):
    DEBUG = False

