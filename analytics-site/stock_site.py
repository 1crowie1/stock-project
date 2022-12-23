from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index(): 
    return render_template("dashboard.html", stock1="TSLA", pos1="78%", neg1="12%")
    # Pass in some example variables to the HTML template


@app.route('/home')
def home():
    return "<div><h1>Stock Analytics</h1></div><div><h2>Displays data analysis and algorithm trading performance</h2></div>"

app.run(host="0.0.0.0", port=5000)