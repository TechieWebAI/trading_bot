from binance.client import Client

API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_API_SECRET"
# Add your Binance Testnet API keys here

client = Client(API_KEY, API_SECRET)
client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'