from flask.ext.wtf import Form
from wtforms import BooleanField, HiddenField, PasswordField, SubmitField, \
					StringField, RadioField, SelectField, TextAreaField
from wtforms import validators, ValidationError

class PeopleProfile(Form):
	fullname = StringField(u'Full Name', [validators.required(), validators.length(max=16)])
	address_default = TextAreaField(u'Primary Address',[validators.optional(), validators.length(max=200)])

	friend_sharing_default = SelectField(u'Sharing with Friends',
								choices=[(u'private',u'Private'),(u'friends',u'Friends'),
									     (u'foaf',u'Friends of Friends'),(u'public',u'Public')])

	neighborhood_sharing_default = RadioField(u'Share with Your Neighborhood', choices=[(True,'Yes'),(False,'No')]) 
	workplace_sharing_default = RadioField(u'Share with Your Workplace', choices=[(True,'Yes'),(False,'No')]) 
	charity_sharing_default = RadioField(u'Share with Charitable Organizations', choices=[(True,'Yes'),(False,'No')]) 

	submit = SubmitField('Save Profile')	
	def validate(self):
		return True
