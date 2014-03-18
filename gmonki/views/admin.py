# -*- coding: utf-8 -*-
"""
	admin.py
"""

from flask import render_template, request, jsonify
from flask.ext.user import login_required, roles_required
from gmonki import app
import os

@app.route('/admin')
@roles_required('admin')   # Use of @roles_required decorator
def admin_page():
    return render_template('admin.html', title="Administration")

# Show Flask configuration vars. ADMINS ONLY!
@app.route('/config')
@roles_required('admin')
def show_flask_config():
    config_response = {'gmonki_config' : os.environ.get('GMONKI_CONFIG', None),
                       'flask_config':{k:str(v) for k,v in app.config.items()},
                       'request.host_url' : request.host_url,
                       'request.url_root' : request.url_root,
                       'app.debug':app.debug}
    return jsonify(config_response)
