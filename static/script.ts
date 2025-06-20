var tickers = JSON.parse(localStorage.getItem('tickers')) || []; // store tickers locally in browser
var lastPrices:{} = {};
var counter:number = 15; // ticker reload

function startUpdateCycle():void {
    
}