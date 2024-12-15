from flask import Blueprint, render_template, abort, request, Response, jsonify
from jinja2 import TemplateNotFound
from parsers import fetch_ticker_details
from models import Stock
import json

stocks_view = Blueprint('stocks_view', __name__, template_folder='templates')

@stocks_view.route('/stocks', methods=['GET', 'POST'])
def all_stocks():
    if request.method == 'GET':
        try:
            result = Stock.objects().to_json(orient="records")
            stocks = json.loads(result)
            return render_template('stocks.html', stocks=stocks)
        except TemplateNotFound:
            abort(404)
    elif request.method == 'POST':
        ticker = request.get_json().get("ticker", None)
        if ticker:
            obj = Stock.filter({'ticker': ticker})
            if obj.empty:
                data = fetch_ticker_details(ticker)
                if data:
                    Stock(data).save()
                    return jsonify({ "message": "Success"})
            else:
                return jsonify({"message": "Stock already exist"})
        return jsonify({"message": "Request Failed"})


@stocks_view.route('/stock/<stock>', methods=['GET', 'PUT'])
def stock_details(stock):
    return render_template('stock.html')
