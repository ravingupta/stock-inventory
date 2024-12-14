from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

stocks_view = Blueprint('stocks_view', __name__, template_folder='templates')

@stocks_view.route('/stock')
def all_stocks():
    try:
        return render_template('stocks.html')
    except TemplateNotFound:
        abort(404)

@stocks_view.route('/stock/<stock>', methods=['GET', 'PUT'])
def stock_details(stock):
    return render_template('stock.html')
