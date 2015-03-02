__author__ = 'mayureshp'

import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    PORT = 5000
    if os.environ["PORT"]:
        PORT = int(os.environ["PORT"])
            
    app.run(port=PORT)