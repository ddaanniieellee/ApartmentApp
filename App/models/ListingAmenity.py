from App.database import db

class ListingAmenity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    listing_id = db.Column(db.Integer, db.ForeignKey('listing.id'), nullable=False)
    amenity_id = db.Column(db.Integer, db.ForeignKey('amenities.id'), nullable=False)


def __init__(self, listing_id, amenity_id):
    self.listing_id = listing_id
    self.amenity_id = amenity_id
    