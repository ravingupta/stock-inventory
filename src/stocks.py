from flask import Blueprint, render_template, abort, request, jsonify
from models import Stock
from parsers import fetch_ticker_details
import json

stocks_view = Blueprint('stocks_view', __name__, template_folder='templates')

@stocks_view.route('/stocks', methods=['GET', 'POST'])
def all_stocks():
    if request.method == 'GET':
        try:
            stocks = json.loads(Stock.objects().to_json(orient="records"))
            return render_template('stocks.html', stocks=stocks)
        except Exception as e:
            print(f"Error fetching stocks: {e}")
            abort(500)
    elif request.method == 'POST':
        payload = request.get_json()
        ticker = payload.get("ticker")
        if not ticker:
            return jsonify({"message": "Ticker is required"}), 400
        try:
            obj = Stock.filter({'ticker': ticker})
            if obj.empty:
                data = fetch_ticker_details(ticker)
                if data:
                    Stock(data).save()
                    return jsonify({"message": "Stock saved successfully"}), 201
                else:
                    return jsonify({"message": "Failed to fetch ticker details"}), 400
            else:
                return jsonify({"message": "Stock already exists"}), 409
        except Exception as e:
            print(f"Error saving stock: {e}")
        return jsonify({"message": "Internal Server Error"}), 500


@stocks_view.route('/stock/<ticker>', methods=['GET', 'PUT'])
def stock_details(ticker):
    if request.method == 'GET':
        try:
            stock = Stock.filter({'ticker': ticker})
            if stock.empty:
                return jsonify({"message": "Stock not found"}), 404
            return stock.to_json(orient="records")
        except Exception as e:
            print(f"Error fetching stock: {e}")
            abort(500)
    elif request.method == 'PUT':
        try:
            stock = Stock.filter({'ticker': ticker})
            if stock.empty:
                return jsonify({"message": "Stock not found"}), 404
            data = fetch_ticker_details(ticker)
            if data:
                Stock(data).save()
                return jsonify({"message": "Stock updated successfully"}), 200
            else:
                return jsonify({"message": "Failed to fetch updated details"}), 400
        except Exception as e:
            print(f"Error updating stock: {e}")
        return jsonify({"message": "Internal Server Error"}), 500
