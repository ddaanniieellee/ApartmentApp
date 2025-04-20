from App.models.user import User
from App.database import db

class Landlord(User):
    __tablename__ = 'landlord'

    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'landlord',
    }

    def __init__(self, username, email, password):
        User.__init__(self, username, email, password, role="landlord")

    def get_json(self):
      return {
        'id': self.id,
        'user': self.user.get_json()
      }  