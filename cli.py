from bot.client import client
import argparse
import logging

logging.basicConfig(
    filename='trading.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def place_order(symbol, side, order_type, quantity, price=None):
    try:
        logging.info(f"Placing Order: {symbol}, {side}, {order_type}, {quantity}, {price}")

        print("\nOrder Summary:")
        print(f"Symbol: {symbol}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Quantity: {quantity}")
        if price:
            print(f"Price: {price}")

        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

        elif order_type == "LIMIT":
            if price is None:
                print("Error: Price required for LIMIT order")
                return

            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )
        else:
            print("Invalid order type")
            return

        print("\nOrder placed successfully!")
        print("Order ID:", order.get("orderId"))
        print("Status:", order.get("status"))
        print("Executed Quantity:", order.get("executedQty"))
        print("Average Price:", order.get("avgPrice"))

        logging.info(f"Order Response: {order}")

    except Exception as e:
        print("Error:", str(e))
        logging.error(f"Error: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    place_order(args.symbol, args.side, args.type, args.quantity, args.price)