from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return { "Message": "Hello this is my docker container message :)", "host": os.uname().nodename}

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)

