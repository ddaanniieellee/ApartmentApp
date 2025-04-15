from .user import create_user
from .landlord import create_landlord
from .tenant import create_tenant
from App.database import db


def initialize():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass')
    jill=create_landlord("jill","jillpass")
    mike=create_tenant("mike","mikepass")
    db.session.add(jill)
    db.session.add(mike)
    db.session.commit()

