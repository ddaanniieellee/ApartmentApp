from App.database import db

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    listing= db.Column(db.Integer, db.ForeignKey('listing.id'), nullable=False)
    street = db.Column(db.String(20), nullable=False)
    city = db.Column(db.String(20), nullable=False )
    lat= db.Column(db.Float, nullable=False)
    lng= db.Column(db.Float, nullable=False)

def __init__(self, listing, street, city, lat, lng):
    self.listing = listing
    self.street = street    #street name  
    self.city = city
    self.lat = lat  # latitude  
    self.lng = lng  # longitude

