from application import db, login_manager
from flask_login import UserMixin
from datetime import datetime


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)
    recipe = db.relationship('Recipe', backref='author', lazy=True)
    
    def __repr__(self):
        return ''.join([
            'User ID: ', str(self.id), '\r\n',
            'Email: ', self.email, '\r\n',
            'Name: ', self.first_name, ' ', self.last_name
        ])



class Cuisine(db.Model):
    cuisine_id = db.Column(db.Integer, primary_key=True,  nullable=False, unique=False)
    cuisine_name= db.Column(db.String(100), nullable=False, unique=False)
    region = db.Column(db.String(100), nullable=False, unique=False)
    recipe = db.relationship('Recipe', backref='cuisine', lazy=True)
    
    def __repr__(self):
         return ''.join([
            'Cuisine: ', self.cuisine, '\r\n',
            'Region: ', self.region, '\r\n',
        
    ])



class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(100), nullable=False, unique=False)
    meal_type = db.Column(db.String(100), nullable=False, unique=False)
    dietary_requirements = db.Column(db.String(100), nullable=False, unique=False)
    difficulty = db.Column(db.String(200), nullable=False, unique=False)
    number_of_servings = db.Column(db.String(200), nullable=False, unique=False)
    ingredients = db.Column(db.String(400), nullable=False, unique=False)
    method = db.Column(db.String(500), nullable=False, unique=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    cuisine_id = db.Column(db.Integer, db.ForeignKey('cuisine.cuisine_id'), nullable=False)
    
    def __repr__(self):
         return ''.join([
            'Recipe Name: ', self.recipe_name, '\r\n',
            'Meal Type: ', self.meal_type, '\r\n',
            'Dietary Requirements: ', self.dietary_requirements, '\r\n',
            'Difficulty: ', self.difficulty, '\r\n',
            'Number Of Servings: ', self.number_of_servings, '\r\n',
            'Ingredients: ', self.ingredients, '\r\n',
            'Method: ', self.method, '\r\n',
            'User ID: ',self.user_id, '\r\n',
    ])




@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))

