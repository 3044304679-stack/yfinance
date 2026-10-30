import yfinance as yf;
import matplotlib.pyplot as plt;
ticker=yf.Ticker("AAPL");
data=ticker.history(period="3mo");
data.to_csv("apple_prices.csv");
print("已保存股价到apple_prices.csv");
plt.figure(figsize=(10,5))
plt.plot(data.index,data["Close"])
plt.title("Apple Close Price (3 months)")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.grid(True)
plt.tight_layout()
plt.savefig("apple_chart.png")
print("✅ 已保存股价图到 apple_chart.png")
