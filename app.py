from flask import Flask

app = Flask(__name__)

# Add this missing home route
@app.route("/")
def home():
    return "Welcome to the Flask App!"

@app.route("/hello")
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)