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
    
    last_row = data.iloc[-1]
    current_price = last_row['Close']
    open_price = last_row['Open']
    change_percent = ((current_price - open_price) / open_price) * 100

    return jsonify({'currentPrice': current_price, 
                    'openPrice': open_price,
                    'changePercent': change_percent}) #compare close and open price

if __name__ == '__main__':
    app.run(debug=True)