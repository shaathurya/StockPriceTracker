import yfinance as yf
from flask import request, render_template, jsonify, Flask

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_stock_data', methods=['POST'])
def get_stock_data():
    ticker = request.get_json()['ticker'] #get ticker field from json object
    data = yf.Ticker(ticker).history(period='1y')
    return jsonify({'currentPrice': data.iloc[-1].Close, #get closing price from the last field
                    'openPrice': data.iloc[-1].Open}) #compare close and open price

if __name__ == '__main__':
    app.run(debug=True)