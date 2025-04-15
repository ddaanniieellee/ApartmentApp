from App.models import Landlord
from App.models import User
from App.models import db

def create_landlord(username,password):
    newuser= Landlord(username=username,password=password)
    db.session.add(newuser)
    db.session.commit()
    return newuser
