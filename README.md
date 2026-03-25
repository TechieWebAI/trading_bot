# Binance Futures Trading Bot (Testnet)

##  Overview
This is a Python-based trading bot that allows you to place **MARKET** and **LIMIT** orders on the Binance Futures Testnet (USDT-M).  
It is designed with a **command-line interface (CLI)**, logging, and robust error handling in a clean and modular structure.

---

## Features

- Place **MARKET** and **LIMIT** orders  
- Supports **BUY** and **SELL** operations  
- **Command-line interface (CLI)** for easy interaction  
- Input validation (price required for LIMIT orders)  
- Logging of API requests and responses  
- Error handling for API and user input issues  

---

## Tech Stack

- Python 3.x  
- [python-binance](https://github.com/sammchardy/python-binance)  
- argparse  
- logging  

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone <your-github-repo-link>
cd trading_bot


2. Install dependencies
pip install python-binance 

3. Setup Binance Testnet API
Go to: Binance Futures Testnet
Create an account and generate API keys
Open bot/client.py and update:
API_KEY = "your_api_key"
API_SECRET = "your_api_secret"



How to Run
MARKET Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
LIMIT Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 68000


Output Example
Order Summary:
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.01

Order placed successfully!
Order ID: 123456
Status: NEW
Executed Quantity: 0.000
Average Price: 0.00

 Logging

All logs are stored in:

trading.log

Includes:

Order request details
API response
Error logs

📁 Project Structure
trading_bot/
  cli.py
  bot/
    client.py
  trading.log
  README.md
  