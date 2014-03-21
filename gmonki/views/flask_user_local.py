# -*- coding: utf-8 -*-
"""
    flask_user_local.py
"""

# usage/activation from gmonki/__init__.py requires
#   from gmonki.views import flask_user_local
#   app.user_manager.unauthorized_view_function = flask_user_local.unauthorized

from flask import current_app, flash, redirect, request, url_for
from flask.ext.user.translations import gettext as _
from gmonki import app
import urlparse

def unauthorized():
    """
    Prepare a Flash message and redirect to USER_UNAUTHORIZED_URL
    """
    # Prepare Flash message
    url = request.script_root + request.path
    flash(_('You do not have MY permission to access %(url)s.', url=url), 'error')

    # Redirect to USER_UNAUTHORIZED_URL
    user_manager = current_app.user_manager
    
    if request.args.get('next'):
        redirect_url = request.host_url + request.values.get('next')
        app.logger.debug('in next: redirect_url ==> ' + redirect_url)
    elif request.referrer and urlparse.urlsplit(request.referrer).netloc == request.host:
        redirect_url = request.referrer
    else:
        redirect_url = user_manager.unauthorized_url if user_manager.unauthorized_url else url_for('profile_page')
    app.logger.debug('redirect_url --> ' + str(redirect_url))
    return redirect(redirect_url)
