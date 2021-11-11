#  import the Flask dependency
from flask import Flask
# create a new Flask app instance
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'
