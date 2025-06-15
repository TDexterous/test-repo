from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/bye')
def bye():
    return "<h1> Bye from Flask Coolify! </h1>"

if __name__ == '__main__':
    app.run(debug=True)
