from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/onboard')
def onboard():
    return render_template('onboarding.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/web-isell')
def isell():
    return render_template('isell.html')

@app.route('/bye')
def bye():
    return "<h1> Bye from WebiSell! </h1>"

if __name__ == '__main__':
    app.run(debug=True)
