from App.models import Landlord
from App.models import User
from App.models import db

def create_landlord(username,email,password):
    newuser= Landlord(username=username,email=email,password=password)
    db.session.add(newuser)
    db.session.commit()
    return newuser
