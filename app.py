from flask import Flask
from src import stocks_view

app = Flask(__name__)
app.register_blueprint(stocks_view)

@app.route("/")
def hello_world():
    return "<p>Welcome to the Stock Inventory Project!</p>"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
