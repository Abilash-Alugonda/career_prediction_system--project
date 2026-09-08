from flask import Flask, request, jsonify, session

from backend.auth import login_user, logout_user
from backend.user_profile import create_profile, get_profile

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


@app.route("/profile", methods=["POST"])
def create_user_profile():

    if "user_id" not in session:
        return jsonify({
            "message": "Please login first"
        }), 401

    data = request.get_json()

    try:

        profile = create_profile(
            session["user_id"],
            data.get("name"),
            data.get("age"),
            data.get("education"),
            data.get("degree"),
            data.get("branch"),
            data.get("skills"),
            data.get("experience"),
            data.get("interests"),
            data.get("preferred_career"),
            data.get("certifications")
        )

        return jsonify({
            "message": "Profile created successfully",
            "profile": profile
        }), 201

    except ValueError as e:

        return jsonify({
            "message": str(e)
        }), 400
@app.route("/profile", methods=["GET"])
def view_profile():

    if "user_id" not in session:
        return jsonify({
            "message": "Please login first"
        }), 401

    try:

        profile = get_profile(session["user_id"])

        return jsonify({
            "profile": profile
        }), 200

    except ValueError as e:

        return jsonify({
            "message": str(e)
        }), 404