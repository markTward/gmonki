from flask.ext.wtf import Form
from wtforms import BooleanField, HiddenField, PasswordField, SubmitField, \
					StringField, RadioField, SelectField, TextAreaField
from wtforms import validators, ValidationError

class PeopleProfile(Form):
	fullname = StringField(u'Full Name', [validators.required(), validators.length(max=16)])
	address_default = TextAreaField(u'Primary Address',[validators.optional(), validators.length(max=200)])
	
