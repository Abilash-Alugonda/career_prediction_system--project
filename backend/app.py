from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Career Prediction System - User Management Module"


if __name__ == "__main__":
    app.run(debug=True)
