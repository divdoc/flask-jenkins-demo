from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask CI/CD!"

@app.route("/hello")
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)