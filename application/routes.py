from flask import render_template, url_for, redirect, request
from application import app, db, bcrypt
from application.models import Recipe, Users
from application.forms import RecipeForm, RegistrationForm, LoginForm, UpdateAccountForm
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/home')
@app.route('/')
def home():
    recipeData = Recipe.query.all()
    return render_template('home.html', title='Home', recipe=recipeData)

@app.route('/about')
def about():
    return render_template('about.html', title='About', desc="This is about food")

@app.route('/register', methods=['GET', 'POST'])
def register():
        if current_user.is_authenticated:
                return redirect(url_for('home'))
        form = RegistrationForm()
        app.logger.info("form instantiated")
        if form.validate_on_submit():
                app.logger.info("forms submiting")
                hash_pw = bcrypt.generate_password_hash(form.password.data)
                user = Users(
                        first_name=form.first_name.data,
                        last_name=form.last_name.data,
                        email=form.email.data,
                        password=hash_pw
			)
        
                db.session.add(user)
                db.session.commit()

                return redirect(url_for('post'))
        else:
            print(form.errors)
        return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		user = Users.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')
			if next_page:
				return redirect(next_page)
			else:
				return redirect('home')
	return render_template('login.html', title='Login', form=form)


@app.route('/post', methods=['GET', 'POST'])
@login_required
def post():
	form = RecipeForm()
	if form.validate_on_submit():
		recipeData = Recipe(
			recipe_name=form.recipe_name.data,
			meal_type=form.meal_type.data,
                        dietary_requirements=form.dietary_requirements.data,
                        difficulty=form.difficulty.data,
                        number_of_servings=form.number_of_servings.data,
                        ingredients=form.ingredients.data,
                        method=form.method.data,
			author=current_user
		)
		db.session.add(recipeData)
		db.session.commit()
		return redirect(url_for('home'))

	else:
		print(form.errors)
	return render_template('post.html', title='Post', form=form)


@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('login'))


@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
	form = UpdateAccountForm()
	if form.validate_on_submit():
		current_user.first_name = form.first_name.data
		current_user.last_name = form.last_name.data
		current_user.email = form.email.data
		db.session.commit()
		return redirect(url_for('account'))
	elif request.method == 'GET':
		form.first_name.data = current_user.first_name
		form.last_name.data = current_user.last_name
		form.email.data = current_user.email
	return render_template('account.html', title='Account', form=form)


@app.route("/account/delete", methods=["GET", "POST"])
@login_required
def account_delete():
        user = current_user.id
        posts = Posts.query.filter_by(user_id=user)
        for post in posts:
                db.session.delete(post)
        account = Users.query.filter_by(id=user).first()
        logout_user()
        db.session.delete(account)
        db.session.commit()
        return redirect(url_for('register'))
