from backend.json_handler import load_users, save_users

users = load_users()

print("Users before:", users)

test_user = {
    "user_id": "TEST001",
    "username": "testuser",
    "email": "test@gmail.com"
}

users.append(test_user)

save_users(users)

print("User saved successfully!")

print("Users after:", load_users())