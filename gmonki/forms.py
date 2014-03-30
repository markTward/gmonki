from flask.ext.wtf import Form
from wtforms import BooleanField, HiddenField, SubmitField, StringField, RadioField, SelectField, TextAreaField
from wtforms import validators, ValidationError

class PeopleProfileForm(Form):
	fullname = StringField(u'Full Name', [validators.required(), validators.length(max=16)])
	address_default = TextAreaField(u'Primary Address',[validators.optional(), validators.length(max=200)])

	friend_sharing_default = RadioField(u'Sharing with Friends',
								choices=[('private','Private'),('friends','Friends'),
									     ('foaf','Friends of Friends'),('public','Public')])

	'''
	neighborhood_sharing_default = RadioField(u'Share with Your Neighborhood', choices=[(True,'Yes'),(False,'No')]) 
	workplace_sharing_default = RadioField(u'Share with Your Workplace', choices=[(True,'Yes'),(False,'No')]) 
	charity_sharing_default = RadioField(u'Share with Charitable Organizations', choices=[(True,'Yes'),(False,'No')]) 
	'''

	next = HiddenField()

	submit = SubmitField('Save Profile')	
