import requests
import json
import time

class Trading212Broker:
    def __init__(self, api_key, environment='demo'):
        self.api_key = api_key
        self.base_url = f"https://{environment}.trading212.com/api/v0"
        self.headers = {
            "Authorization": f"Basic {api_key}"
        }

    def get_cash_balance(self):
        """Retrieves account cash information."""
        response = requests.get(f"{self.base_url}/equity/account/cash", headers=self.headers)
        return response.json()

    def get_portfolio(self):
        """Retrieves current open positions."""
        response = requests.get(f"{self.base_url}/equity/portfolio", headers=self.headers)
        return response.json()

    def place_market_order(self, ticker, quantity):
        """Places a market order. Positive quantity for BUY, negative for SELL."""
        payload = {
            "quantity": quantity,
            "ticker": ticker
        }
        response = requests.post(f"{self.base_url}/equity/orders/market", headers=self.headers, json=payload)
        return response.json()

    def get_orders(self):
        """Retrieves all pending orders."""
        response = requests.get(f"{self.base_url}/equity/orders", headers=self.headers)
        return response.json()

if __name__ == "__main__":
    # Example usage (demo key needed)
    print("Trading 212 Broker Logic Initialized.")
