from backend.auth import register_user

try:
    user = register_user(
        "abilash123",
        "abilash@gmail.com",
        "Abilash@123"
    )

    print("Registration successful!")
    print("User ID:", user["user_id"])
    print("Username:", user["username"])
    print("Email:", user["email"])

except ValueError as e:
    print("Registration failed:", e)