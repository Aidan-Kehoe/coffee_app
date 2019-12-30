from app import db
from app import login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(id):
	return User.query.get(int(id))

class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(64), index = True, unique = True)
	email = db.Column(db.String(120), index = True, unique = True)
	password_hash = db.Column(db.String(128))
	reviews = db.relationship('Review', backref='author', lazy='dynamic')
	about_me = db.Column(db.String(140))
	last_seen = db.Column(db.DateTime, default=datetime.utcnow)

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)
	
	def my_posts(self):
		own = Review.query.filter_by(user_id=self.id)
		return own.order_by(Review.timestamp.desc())

	def __repr__(self):
		return '<User {}>'.format(self.username)

class Review(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64))
	origin = db.Column(db.String(64))
	altitude = db.Column(db.Integer)
	process = db.Column(db.String(64))
	grind = db.Column(db.Float)
	espresso = db.Column(db.Boolean, default = 0)
	tasting = db.Column(db.String(120))
	review = db.Column(db.Float)
	timestamp = db.Column(db.DateTime, index = True, default = datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return '{}'.format(self.name, self.origin, self.process, self.altitude, self.grind, self.espresso, self.tasting, self.review)