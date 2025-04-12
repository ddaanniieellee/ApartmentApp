from App.database import  db

class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)  
    title = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    bedrooms = db.Column(db.Integer, nullable=False)
    bathrooms = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  
    location = db.relationship('Location', backref='listing', uselist=False)
    amenities = db.relationship('ListingAmenity', backref='listing', lazy=True)
    user = db.relationship('User', backref='listing', lazy=True)  

def __init__(self, title, description, price, bedrooms, bathrooms, user_id, location):
    self.title = title
    self.description = description  
    self.price = price
    self.bedrooms = bedrooms
    self.bathrooms = bathrooms
    self.user_id = user_id  
    self.location = location
  
  
