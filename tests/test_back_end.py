import unittest

from flask import url_for
from flask_testing import TestCase

from application import app, db, bcrypt
from application.models import Users, Recipe, Cuisine
from os import getenv



class TestBase(TestCase):

    def create_app(self):
        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_URI'),
                SECRET_KEY=getenv('TEST_KEY'),
                WTF_CSRF_ENABLED=False,
                DEBUG=True
                )
        return app

    def setUp(self):
        db.session.commit()
        db.drop_all()
        db.create_all()


        hashed_pw = bcrypt.generate_password_hash('admin2016')
        admin = Users(first_name="admin", last_name="admin", email="admin@admin.com", password=hashed_pw)

        hashed_pw_2 = bcrypt.generate_password_hash('test2016')
        employee = Users(first_name="test", last_name="user", email="test@user.com", password=hashed_pw_2)

        db.session.add(admin)
        db.session.add(employee)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()



class TestViews(TestBase):

    def test_home(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)


    def test_about(self):
        response = self.client.get(url_for('about'))
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.client.get(url_for('login'))
        self.assertEqual(response.status_code, 200)


    def test_register(self):
        response = self.client.get(url_for('register'))
        self.assertEqual(response.status_code, 200)


class TestRecipe(TestBase):
    
    def test_add_new_recipe(self):
        with self.client:
            self.client.post(
                    '/login',
                    data=dict(
                        email='test@test.com',
                        password='test'),
                    )
            response = self.client.post(
                    '/recipe',
                    data=dict(
                        recipe_name='Recipe Name',
                        meal_type='Meal Type',
                        dietary_requirements='Dietary Requirements',
                        difficulty='Difficulty',
                        number_of_servings='Number Of Servings',
                        ingredients='Ingredients',
                        method='Method',
                        cuisine='Cuisine'
                    ),
                    follow_redirects=True
                )
            self.assertIn(b'New Recipe', response.data)


class TestCuisine(TestBase):

    def test_add_new_cuisine(self):
        with self.client:
            self.client.post(
                    '/login',
                    data=dict(
                        email='test@test.com',
                        password='test'),
                    )
            response = self.client.post(
                    '/cuisine',
                    data=dict(
                        cuisine_name='Cuisine Name',
                        region='Region'
                    ),
                    follow_redirects=True
                )
            self.assertIn(b'New Cuisine', response.data)


class TestRegister(TestBase):

    def test_register(self):
        with self.client:
            response = self.client.post(
                    '/register',
                    data = dict(
                        first_name="testfirst",
                        last_name="testlast",
                        email="test@testing.com",
                        password="testing",
                        ),
                    follow_redirects=True
                    )
            self.assertIn(b'testfirst', response.data)
            self.assertIn(b'testlast', response.data)
            self.assertIn(b'test@testing.com', response.data)


class RecipeUpdate(TestBase):

    def recipe_test_update(self):
        with self.client:
            self.client.post(
                    '/login',
                    data=dict(
                        email='test@test.com',
                        password='test'),
                    )
            self.client.post(
                    '/recipe',
                    data=dict(
                        recipe_name='Recipe Name',
                        meal_type='Meal Type',
                        dietary_requirements='Dietary Requirements',
                        difficulty='Difficulty',
                        number_of_servings='Number Of Servings',
                        ingredients='Ingredients',
                        method='Method',
                        cuisine='Cuisine'
                    ),
                )
            response = self.client.post(
                    '/update',
                    data=dict(
                        recipe_name='New Recipe Name',
                        meal_type='New Meal Type',
                        dietary_requirements='New Dietary Requirements',
                        difficulty='New Difficulty',
                        number_of_servings='New Number Of Servings',
                        ingredients='New Ingredients',
                        method='New Method',
                        cuisine='New Cuisine',
                    follow_redirects=True
                    ))
            self.assertIn(b'New Recipe', response.data)


class TestLogout(TestBase):

    def test_logout(self):
        with self.client:
            self.client.post(
                    '/login',
                    data=dict(
                        email='test@test.com',
                        password='test'),
                    )
            response = self.client.get('/logout', follow_redirects=True)
            self.assertIn(b"login", response.data)

class AccountUpdate(TestBase):
    def account_test_update(self):
        with self.client:
            self.client.post(
                    '/login',
                    data=dict(
                        email='test@test.com',
                        password='test'),
                    )
            self.client.post(
                    '/account',
                    data=dict(
                        first_name='First Name',
                        last_name='Last Name',
                        email='Email'
                    ),
                )
            response = self.client.post(
                    '/account',
                    data=dict(
                        first_name='New First Name',
                        last_name='New Last Type',
                        email='Email',
                    follow_redirects=True
                    ))
            self.assertIn(b'Updated Account', response.data)
