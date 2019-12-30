from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, IntegerField, FloatField, \
SelectField
from app import app
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from app.models import User

class LoginForm(FlaskForm):
	username = StringField('Username', validators = [DataRequired()])
	password = PasswordField('Password', validators = [DataRequired()])
	remember_me = BooleanField('Remember Me')
	submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	password2 = PasswordField(
		'Repeat Password', validators = [DataRequired(), EqualTo('password')])
	submit = SubmitField('Register')

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user is not None:
			raise ValidationError('Please use a different username.')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user is not None:
			raise ValidationError('Please use a different email address.')

class EditProfileForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	about_me = TextAreaField('About me', validators = [Length(min=0, max=200)])
	submit = SubmitField('Submit')

	def __init__(self, original_username, *args, **kwargs):
		super(EditProfileForm, self).__init__(*args, **kwargs)
		self.original_username = original_username

	def validate_username(self, username):
		if username.data != self.original_username:
			user = User.query.filter_by(username=self.username.data).first()
			if user is not None:
				raise ValidationError('Please use a different username.')

class ReviewForm(FlaskForm):
	name = StringField('Coffee Name', validators = [DataRequired()])
	origin = StringField('Coffee Origin', validators = [DataRequired()])
	origing = StringField('Coffee Processing Type')
	altitude = IntegerField('Altitude', validators = [DataRequired()])
	grind = FloatField('Grind Setting', validators = [DataRequired()])
	espresso = BooleanField('Espresso')
	tasting = TextAreaField('Tasting Notes', validators=[Length(min=0, max = 200)])
	review = IntegerField('1-10 Review', validators=[DataRequired()])
	submit = SubmitField('Submit')

class PredictForm1(FlaskForm):
	origin = SelectField('Country of Origin', choices = app.config['ORIGINS'], validators = [DataRequired()])
	altitude = IntegerField('Altitude', validators = [DataRequired()])
	origing = SelectField('Roasting Process', choices = app.config['PROCESS'], validators = [DataRequired()])
	submit = SubmitField('Predict!')