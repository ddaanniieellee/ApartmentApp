from App.models import Tenant
from App.models import User
from App.models import db

def create_tenant(username,password):
    newuser= Tenant(username=username,password=password)
    db.session.add(newuser)
    db.session.commit()
    return newuser