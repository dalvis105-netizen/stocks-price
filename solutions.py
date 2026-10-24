# Import yfinance library
import yfinance as yf

# List of stock symbols
stocks = ["HDFCBANK.NS", "RELIANCE.NS", "TCS.NS", "ITC.NS"]

# Download last 30 days of stock data
for stock in stocks:

    print("Stock:", stock)

    data = yf.download(stock, period="30d", progress=False)

    # Display closing prices
    print(data["Close"])

    # Save data in CSV file
    data["Close"].to_csv(stock + ".csv")

print("Download completed!")