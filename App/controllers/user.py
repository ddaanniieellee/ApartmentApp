from App.models import User
from App.database import db

def create_user(username, email, password):
    if not username or not password:
        raise ValueError("Username and password are required.")
    email = email or f"{username}@example.com"  # Fallback for tests
    existing_user = get_user_by_username(username)
    if existing_user:
        raise ValueError(f"User with username '{username}' already exists.")
    newuser = User(username=username, email=email, password=password)
    db.session.add(newuser)
    db.session.commit()
    return newuser

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user(id):
    return User.query.get(id)

def get_all_users():
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    return [user.get_json() for user in users if user]

def update_user(id, username):
    user = get_user(id)
    if not user:
        raise ValueError(f"User with ID '{id}' not found.")
    if not username:
        raise ValueError("Username cannot be empty.")
    user.username = username
    db.session.add(user)
    db.session.commit()
    return user