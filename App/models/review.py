from App.database import db

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    listing_id = db.Column(db.Integer, db.ForeignKey('listing.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(120), nullable=False)
    

def __init__(self, listing_id, user_id, rating, comment):
    self.listing_id = listing_id
    self.user_id = user_id
    self.rating = rating
    self.comment = comment
    