from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to Flask running inside Docker!</h1>"

@app.route("/about")
def about():
    return "<h2>This application is running in a Docker container.</h2>"

@app.route("/health")
def health():
    return {
        "status": "Running",
        "application": "Flask",
        "container": "Docker"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    