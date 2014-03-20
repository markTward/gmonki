# -*- coding: utf-8 -*-
"""
	admin.py
"""

from flask import render_template, request, json
from flask.ext.user import login_required, roles_required, current_user
from gmonki import app
import os

def get_pretty_print(json_object):
    return json.dumps(json_object, sort_keys=True, indent=4, separators=(',', ': '))

@app.route('/admin')
@roles_required('admin')   # Use of @roles_required decorator
def admin_page():
    return render_template('admin.html', title="Administration")

@app.route('/config')
@roles_required('admin')
def show_flask_config():
    config_data = {'gmonki_config' : os.environ.get('GMONKI_CONFIG', None),
                   'flask_config':{k:str(v) for k,v in app.config.items()},
                   'request.host_url' : request.host_url,
                   'request.url_root' : request.url_root,
                   'app.debug':app.debug}
    return render_template('config.html', 
							title='Flask Configuration', 
							config_data = json.dumps(config_data, sort_keys=True, indent=4, separators=(',' ,': ')))

@app.route('/current_user')
@roles_required('admin')
def show_current_user():
    exclude_list = ['has_roles','roles', 'query', 'query_class']
    #current_user_data = {'current_user_data':{attr:getattr(current_user,attr) for attr in dir(current_user) if not attr.startswith('_') and attr not in exclude_list }}
    return render_template('current_user.html', 
							title='current_user attributes & methods')
							#current_user_data = current_user_data)
							#current_user_data = json.dumps(current_user_data, sort_keys=True, indent=4, separators=(',' ,': ')))

