from App.models.user import User

class Landlord(User):
  table_name = 'landlord'
  __mapper_args__ ={'polymorphic_identity':'landlord'}

