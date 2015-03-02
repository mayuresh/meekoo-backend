__author__ = 'mayureshp'

import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(port= os.environ["PORT"] | 5000)