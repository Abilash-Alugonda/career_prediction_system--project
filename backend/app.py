from flask import Flask, request, jsonify, session

from backend.auth import login_user, logout_user

app = Flask(__name__)

app.secret_key = "change-this-secret-key"


@app.route("/")
def home():
    return "Career Prediction System - User Management Module"


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    username_or_email = data.get("username_or_email")
    password = data.get("password")

    try:
        user = login_user(
            username_or_email,
            password
        )

        session["user_id"] = user["user_id"]
        session["username"] = user["username"]

        return jsonify({
            "message": "Login successful",
            "user": user
        }), 200

    except Exception as e:
        return jsonify({
            "message": str(e)
        }), 401


@app.route("/logout", methods=["POST"])
def logout():
    session.clear()

    return jsonify({
        "message": "Logout successful"
    }), 200


if __name__ == "__main__":
    app.run(debug=True)