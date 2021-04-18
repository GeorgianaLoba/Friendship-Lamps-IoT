import os

from flask import Flask

app = Flask(__name__)
dict = {"option": 1}


@app.route("/hello", methods=["GET"])
def hello():
    """Method 1: Return a simple hello"""
    return "Hello", 200

@app.route("/getopt", methods=["GET"])
def getOption():
    return {"option": dict["option"]}, 200


@app.route("/setopt/<opt>", methods=["GET"])
def setOption(opt):
    dict["option"] = int(opt)
    return {"option":  dict["option"]}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 8080)))