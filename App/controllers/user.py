from App.models import User
from App.database import db

def create_user(username, email, password):
    if not username or not password:
        raise ValueError("Username and password are required.")
    if not email:
        raise ValueError("Email is required.")
    
    # Check if username already exists
    existing_user = get_user_by_username(username)
    if existing_user:
        raise ValueError(f"User with username '{username}' already exists.")
    
    # Check if email already exists
    existing_email = User.query.filter_by(email=email).first()
    if existing_email:
        raise ValueError(f"User with email '{email}' already exists.")
    
    # Create and save the new user
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
    
    # Check for username conflicts
    existing_user = get_user_by_username(username)
    if existing_user and existing_user.id != id:
        raise ValueError(f"Username '{username}' is already taken by another user.")
    
    user.username = username
    db.session.add(user)
    db.session.commit()
    return user