# -*- coding: utf-8 -*-
from gmonki import app, db, User, Role, user_manager

# initialize / reset db
db.create_all()

# Make some 'play' roles for testing
secret_role = Role(name='secret')
agent_role = Role(name='agent')
admin_role = Role(name='admin')

# Create test users if they don't exist
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

