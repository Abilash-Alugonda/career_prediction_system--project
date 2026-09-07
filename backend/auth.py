from backend.validation import (
    validate_username,
    validate_email,
    validate_password       # Build Registration
)

from backend.json_handler import load_users, save_users

from werkzeug.security import generate_password_hash

def generate_user_id(users):    #Create User ID Generator
    return f"USR{len(users) + 1:03d}"

def username_exists(users, username):  #Create Duplicate Username Check
    return any(
        user["username"].lower() == username.lower()
        for user in users
    )

def email_exists(users, email):   #Create Duplicate Email Check
    return any(
        user["email"].lower() == email.lower()
        for user in users
    )
users = []
def register_user(username, email, password):  #Create the Registration Function
    def register_user(username, email, password):

     users = load_users()

    if not validate_username(username):
        raise ValueError("Invalid username")

    if not validate_email(email):
        raise ValueError("Invalid email")

    if not validate_password(password):
        raise ValueError(
            "Password must contain uppercase, lowercase, "
            "number, special character and be at least 8 characters"
        )

    if username_exists(users, username):
        raise ValueError("Username already exists")

    if email_exists(users, email):
        raise ValueError("Email already registered")

    user_id = generate_user_id(users)

    password_hash = generate_password_hash(password)

    new_user = {
        "user_id": user_id,
        "username": username,
        "email": email,
        "password_hash": password_hash
    }

    users.append(new_user)

    save_users(users)

    return new_user
    