# -*- coding: utf-8 -*-
from gmonki import app
from flask.ext.user.signals import user_confirmed_email
from gmonki import dbservice

@user_confirmed_email.connect_via(app)
def user_confirmed_email_action(sender, user, **extra):
    sender.logger.info('SIGNAL user_confirmed_email: ' + str(sender.name) + ' ' + str(user.username))
	# create or merge unique neo4j node on User.username
    try:
        dbservice.get_graph_db()
    except:
        sender.logger.error('create_gmonki_graph_user: ERROR get_graph_db()')

