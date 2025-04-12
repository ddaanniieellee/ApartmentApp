from App.models.user import User

class Tenant(User):
  table_name = 'tenant'
  __mapper_args__ ={'polymorphic_identity':'tenant'}

