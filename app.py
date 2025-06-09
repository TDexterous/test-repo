from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1> Hello from Flask Coolify! </h1>"


@app.route('/bye')
def bye():
    return "<h1> Bye from Flask Coolify! </h1>"