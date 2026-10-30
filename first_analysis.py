import yfinance as yf;
ticker=yf.Ticker("AAPL");
data=ticker.history(period="1mo");
print(data)
