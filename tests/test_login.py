from backend.auth import login_user

try:
    result = login_user(
        "abilash123",
        "Abilash@123"
    )

    print("Login successful!")
    print("User ID:", result["user_id"])
    print("Username:", result["username"])
    print("Email:", result["email"])

except ValueError as e:
    print("Login failed:", e)