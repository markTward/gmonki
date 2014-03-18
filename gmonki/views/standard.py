# -*- coding: utf-8 -*-
"""
	standard.py
"""

from flask import render_template_string, url_for
from gmonki import app
from flask.ext.user import login_required, roles_required

# The '/' page is accessible to anyone
@app.route('/')
@app.route('/index')
def index():
    return render_template_string("""
        {% extends "base.html" %}
        {% block content %}
        <h2>{%trans%}Home Page{%endtrans%}</h2>
		{% if current_user.username == null %}
        	<p><a href="{{ url_for('user.login') }}">{%trans%}Sign in{%endtrans%}</a></p>
		{% else %}
        	<p><a href="{{ url_for('user.logout') }}">{%trans%}Sign out{%endtrans%}</a></p>
		{% endif %}
        {% endblock %}
        """)

# The '/profile' page requires a logged-in user
@app.route('/profile')
@login_required                                 # Use of @login_required decorator
def profile_page():
    return render_template_string("""
        {% extends "base.html" %}
        {% block content %}
        <h2>{%trans%}PROFILE Page{%endtrans%}</h2>
        <p> {%trans%}Hello{%endtrans%}
            {{ current_user.username or current_user.email }},</p>
        <p> <a href="{{ url_for('user.change_username') }}">
            {%trans%}Change username{%endtrans%}</a></p>
        <p> <a href="{{ url_for('user.change_password') }}">
            {%trans%}Change password{%endtrans%}</a></p>
        <p> <a href="{{ url_for('user.logout') }}?next={{ url_for('user.login') }}">
            {%trans%}Sign out{%endtrans%}</a></p>
        {% endblock %}
        """)

# The '/special' page requires a user that has the 'special' AND ('sauce' OR 'agent') role.
@app.route('/special')
@roles_required('secret', ['sauce', 'agent'])   # Use of @roles_required decorator
def special_page():
    return render_template_string("""
        {% extends "base.html" %}
        {% block content %}
        <h2>{%trans%}Special Page{%endtrans%}</h2>
        {% endblock %}
        """)

