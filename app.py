from flask import Flask
from src import stocks_view

app = Flask(__name__)
app.register_blueprint(stocks_view)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
