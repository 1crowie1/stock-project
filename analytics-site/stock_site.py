from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return "<div><h1>Stock Analytics</h1></div><div><h2>Displays data analysis and algorithm trading performance</h2></div>"
