from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    # check commit hash, pull and checkouts
    # send mail that testing started
    # send mail with testing results
    return 'Hello, World!'
