import logging

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
from werkzeug.security import check_password_hash
from backend.validation import (
    validate_username,
    validate_email,
    validate_password       # Build Registration
)

from backend.json_handler import load_users, save_users

from werkzeug.security import generate_password_hash
login_attempts = {}
MAX_LOGIN_ATTEMPTS = 5

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

def find_user(users, username_or_email):
    for user in users:
        if (
            user["username"].lower() == username_or_email.lower()
            or
            user["email"].lower() == username_or_email.lower()
        ):
            return user

    return None
def login_user(username_or_email, password):
    users = load_users()

    user = find_user(users, username_or_email)

    if user is None:
        raise ValueError("Invalid username/email or password")

    username = user["username"]

    if user.get("locked", False):
        raise ValueError("Account is locked")

    attempts = login_attempts.get(username, 0)

    if attempts >= MAX_LOGIN_ATTEMPTS:
        user["locked"] = True
        save_users(users)
        raise ValueError("Account is locked")

    if not check_password_hash(user["password_hash"], password):
        attempts += 1
        login_attempts[username] = attempts

        if attempts >= MAX_LOGIN_ATTEMPTS:
            user["locked"] = True
            save_users(users)
            raise ValueError("Too many failed attempts. Account locked")

        remaining = MAX_LOGIN_ATTEMPTS - attempts

        raise ValueError(
            f"Invalid username/email or password. "
            f"Attempts remaining: {remaining}"
        )

    login_attempts[username] = 0

    return {
        "user_id": user["user_id"],
        "username": user["username"],
        "email": user["email"]
    }
def logout_user():
    return {
        "message": "Logout successful"
    }