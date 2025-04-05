



from smartapi import SmartConnect

API_KEY = "your_api_key"
CLIENT_ID = "your_client_id"
PASSWORD = "your_password"
TOTP = "your_totp_here"

obj = SmartConnect(api_key=API_KEY)

data = obj.generateSession(CLIENT_ID, PASSWORD, TOTP)
auth_token = data['data']['jwtToken']
feed_token = obj.getfeedToken()

print("Login Successful!")
print("Feed Token:", feed_token)

orderparams = {
    "variety": "NORMAL",
    "tradingsymbol": "SBIN-EQ",
    "symboltoken": "3045",
    "transactiontype": "BUY",
    "exchange": "NSE",
    "ordertype": "LIMIT",
    "producttype": "INTRADAY",
    "duration": "DAY",
    "price": "650",
    "quantity": "1"
}

orderId = obj.placeOrder(orderparams)
print("Order placed successfully, Order ID:", orderId)


