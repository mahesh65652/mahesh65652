## Hi there 👋

<!--
import requests
import time

# Angel One API Credentials (Replace with your own)
API_KEY = "your_api_key"
CLIENT_ID = "your_client_id"
FEED_TOKEN = "your_feed_token"
BASE_URL = "https://apiconnect.angelbroking.com/rest/"

# Headers for API requests
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-UserType": "USER",
    "X-SourceID": "WEB",
    "X-ClientLocalIP": "127.0.0.1",
    "X-ClientPublicIP": "127.0.0.1",
    "X-MACAddress": "00:00:00:00:00:00",
    "X-PrivateKey": API_KEY,
    "X-ClientID": CLIENT_ID,
    "Authorization": f"Bearer {FEED_TOKEN}"
}

# Fetch Nifty 50 Live Data
def get_nifty_data():
    url = BASE_URL + "v1/marketdata/instruments/quotes"
    payload = {
        "exchange": "NSE",
        "symboltoken": "99926000",  # Nifty 50 Token
    }
    response = requests.post(url, json=payload, headers=HEADERS)
    if response.status_code == 200:
        data = response.json()
        if "data" in data:
            ltp = data["data"]["ltp"]
            print(f"Nifty 50 LTP: {ltp}")
            return ltp
    print("Failed to fetch Nifty data")
    return None

# Simple Moving Average Strategy
def moving_average_strategy():
    prices = []
    while True:
        price = get_nifty_data()
        if price:
            prices.append(price)
            if len(prices) > 10:
                prices.pop(0)
            sma = sum(prices) / len(prices)
            print(f"SMA: {sma}")
            if price > sma:
                print("BUY Signal")
            elif price < sma:
                print("SELL Signal")
        time.sleep(10)  # Fetch data every 10 seconds

if __name__ == "__main__":
    moving_average_strategy()

