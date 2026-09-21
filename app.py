from flask import Flask

# Initialize the app FIRST
app = Flask(__name__)


# THEN define your routes
@app.route("/hello")
def hello():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True)