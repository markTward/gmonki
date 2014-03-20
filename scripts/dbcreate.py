# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
from gmonki import app, db, User, Role, user_manager

# initialize / reset db
db.create_all()

# Make some 'play' roles for testing
user_role = Role(name='user')
admin_role = Role(name='admin')

# Create test users
user1 = User(username='user007', email='007@marktward.name', active=True, 
			 password=user_manager.password_crypt_context.encrypt('Password1'))
user1.roles.append(user_role)
db.session.add(user1)

user2 = User(username='Queue', email='Q@marktward.name', active=True,
        password=user_manager.password_crypt_context.encrypt('Password1'))
user2.roles.append(user_role)
user2.roles.append(admin_role)
db.session.add(user2)

# commit all db entries
db.session.commit()

