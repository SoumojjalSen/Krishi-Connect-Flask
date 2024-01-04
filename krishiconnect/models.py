from . import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(10), nullable=False)
    pincode = db.Column(db.String(6), nullable=False)
    state = db.Column(db.String(2), nullable=False)

class Community(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    item = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    cost =  db.Column(db.Float, nullable=False)
    
    def __repr__(self):
        # return f"User('{self.id}', '{self.lender_name})"
        return f"Community('{self.id}', {self.quantity}', '{self.machinery}', '{self.cost}')"
    
class Harvest(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    user_id = db.Column(db.Integer, nullable=False)   
    crop_name = db.Column(db.String(10), nullable=False)
    quantity = db.Column(db.Float, nullable=False)

class Livestock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    livestock_name = db.Column(db.String(10), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
     
