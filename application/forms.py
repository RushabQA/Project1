from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import Users
from flask_login import current_user

class RecipeForm(FlaskForm):
    recipe_name = StringField('Recipe name',
        validators = [
            DataRequired(),
            Length(min=2, max=100)
        ]
    )
    meal_type = StringField('Meal Type',
        validators = [
            DataRequired(),
            Length(min=2, max=100)
        ]
    )
    dietary_requirements = StringField('Dietary Requirements',
        validators = [
            DataRequired(),
            Length(min=2, max=100)
        ]
    )
    difficulty = StringField('Difficulty',
        validators = [
            DataRequired(),
            Length(min=2, max=200)
        ]
    )
    number_of_servings = StringField('Number Of Servings',
        validators = [
            DataRequired(),
            Length(min=2, max=200)
        ]
    )
    ingredients = StringField('Ingredients',
        validators = [
            DataRequired(),
            Length(min=2, max=400)
        ]
    )
    method = StringField('Method',
        validators = [
            DataRequired(),
            Length(min=2, max=500)
        ]
    )
    submit = SubmitField('Post!')


class RegistrationForm(FlaskForm):
    first_name = StringField('First Name',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    last_name = StringField('Last Name',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )

    email = StringField('Email',
        validators = [
            DataRequired(),
            Email()
        ]
    )
    password = PasswordField('Password',
        validators = [
            DataRequired()
        ]
    )
    confirm_password = PasswordField('Confirm Password',
        validators = [
            DataRequired(),
            EqualTo('password')
        ]
    )
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('Email already in use')


class LoginForm(FlaskForm):
    email = StringField('Email',
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField('Password',
        validators=[
            DataRequired()
        ]
    )

    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    first_name = StringField('First Name',
        validators=[
            DataRequired(),
            Length(min=4, max=30)
        ])
    last_name = StringField('Last Name',
        validators=[
            DataRequired(),
            Length(min=4, max=30)
        ])
    email = StringField('Email',
        validators=[
            DataRequired(),
            Email()
        ])
    submit = SubmitField('Update')

    def validate_email(self,email):
        if email.data != current_user.email:
            user = Users.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email already in use')
