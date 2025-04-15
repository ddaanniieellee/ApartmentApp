from App.models.user import User
from App.database import db

class Landlord(User):
  table_name = 'Landlord'
  __mapper_args__ ={'polymorphic_identity':'Landlord'}

def __init__(self,username,password):
  super.__init__(username,password)