from application import db
from application.models import Recipe, Users, Cuisine

db.drop_all()
db.create_all()
