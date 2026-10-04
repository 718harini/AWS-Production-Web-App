from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home():
    return "Backend works!"


@app.route("/api/users", methods=["POST"])
def create_user():
    data = request.json

    if not data:
        return "No data provided", 400

    name = data.get("name")
    email = data.get("email")

    if not name or not email:
        return "Name and email are required", 400

    return f"Name: {name}, Email: {email}"


if __name__ == "__main__":
    app.run(debug=True)