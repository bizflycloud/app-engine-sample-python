from flask import Flask

app = Flask(__name__)


@app.get("/")
def index():
    return "This is your first Python app run on App Engine Bizfly Cloud!"


if __name__ == "__main__":
    # Dev only: run "python main.py" and open http://localhost:8080
    app.run(host="0.0.0.0", port=8080, debug=True)
