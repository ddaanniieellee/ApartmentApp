from App.models.user import User
from App.database import db

class Tenant(db.Model):
    tenant_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('tenant', uselist=False), foreign_keys=[user_id])

    def __init__(self, user_id):
        self.user_id = user_id

    def get_json(self):
        return {
            'id': self.id,
            'user': self.user.get_json()
        }
    
    table_name = 'Tenant'
    __mapper_args__ = {'polymorphic_identity': 'Tenant'}
