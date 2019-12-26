from app import app, db
from flask import render_template, flash, redirect, request, url_for
from app.forms import LoginForm, RegistrationForm, EditProfileForm, ReviewForm, PredictForm1#, PredictForm2
from app.models import User, Review
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from datetime import datetime
import numpy as np
import pickle

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
	form = ReviewForm()
	if form.validate_on_submit():
		review = Review(name=form.name.data, origin=form.origin.data, altitude=form.altitude.data,
			grind=form.grind.data, espresso=form.espresso.data, tasting=form.tasting.data, 
			review=form.review.data, author=current_user)
		db.session.add(review)
		db.session.commit()
		flash('Nice review, super pretentious, you nailed it.')
		return redirect('/index')
	return render_template('index.html', title = 'Home Page', form = form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect('/index')
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user is None or not user.check_password(form.password.data):
			flash("Invalid username or password. Or maybe this website fucked up. Who knows ¯\\_(ツ)_/¯")
			return redirect('/login')
		login_user(user, remember=form.remember_me.data)
		next_page = request.args.get('next')
		if not next_page or url_parse(next_page).netloc != '':
			next_page = '/index'
		return redirect(next_page)
	return render_template('login.html', title = 'Sign In', form = form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect('/index')

@app.route('/register', methods = ['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect('/index')
	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(username=form.username.data, email=form.email.data)
		user.set_password(form.password.data)
		db.session.add(user)
		db.session.commit()
		flash("Congratulations, you have logged in. Even though you're the only user. But whatever... go nuts")
		return redirect('/login')
	return render_template('register.html', title='Register', form = form)

@app.route('/user/<username>')
@login_required
def user(username):
	user = User.query.filter_by(username = username).first_or_404()
	page = request.args.get('page', 1, type=int)
	reviews = current_user.my_posts().paginate(page, app.config['POSTS_PER_PAGE'], False)
	next_url = url_for('index', page=reviews.next_num) if reviews.has_next else None
	prev_url = url_for('index', page=reviews.prev_num) if reviews.has_prev else None
	return render_template('user.html', user = user, reviews = reviews.items, next_url=next_url,
						   prev_url=prev_url)

@app.before_request
def before_request():
	if current_user.is_authenticated:
		current_user.last_seen = datetime.utcnow()
		db.session.commit()

@app.route('/edit_profile', methods = ['GET', 'POST'])
@login_required
def edit_profile():
	form = EditProfileForm(current_user.username)
	if form.validate_on_submit():
		current_user.username = form.username.data
		current_user.about_me = form.about_me.data
		db.session.commit()
		flash('Your changes have been saved, narcissist.')
		return redirect(url_for('edit_profile'))
	elif request.method == 'GET':
		form.username.data = current_user.username
		form.about_me.data = current_user.about_me
	return render_template('edit_profile.html', title = 'Edit Profile', form = form)

@app.route('/explore')
@login_required
def explore():
	#reviews = Review.query.order_by(Review.timestamp.desc()).all()
	return render_template('index.html', title='Explore')#, reviews=reviews)

@app.route('/predict',methods=['GET','POST'])
@login_required
def predict():
	form = PredictForm1()
	#form_2 = PredictForm2()
	#int_features = [int(x) for x in request.form.values()]
	#final_features = [np.array(int_features)]
	#prediction = model.predict(final_features)
	origin = form.origin.data
	altitude = form.altitude.data
	process = form.origing.data
	loaded_model = pickle.load(open('./data/model.pkl', 'rb'))
	prediction = loaded_model.predict(final_features)

	#output = round(prediction[0], 2)
	output = "HI"

	return render_template('predict.html', prediction_text='Sales should be $ {}'.format(output), form1=form_1)