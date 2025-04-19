from App.models.user import User
from App.database import db

class Landlord(User):

  landlord_id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  user = db.relationship('User', backref=db.backref('landlord', uselist=False), foreign_keys=[user_id]) 

  def __init__(self, user_id):
      self.user_id = user_id

  def get_json(self):
      return {
        'id': self.id,
        'user': self.user.get_json()
      }  
  
  table_name = 'Landlord'
  __mapper_args__ ={'polymorphic_identity':'Landlord'}
  

def __init__(self,username,password):
  super.__init__(username,password)