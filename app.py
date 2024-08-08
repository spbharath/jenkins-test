from flask import Flask, json

app = Flask(__name__)


@app.route("/")
def home():
    return "Hi welcome to Jenkins Testing"


@app.route("/hi/<name>", methods=["GET"])
def say_hi(name):
    return {"message": f"Hi, I am {name}", "number": 10, "boolean": True}


@app.route("/bye", methods=["GET"])
def say_bye():
    return {"message": "Bye!", "number": 10, "boolean": True}


if __name__ == "__main__":
    app.run(5000, debug=True)
