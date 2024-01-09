import yfinance as yf


class Asset:
    def __init__(self, symbol):
        self.yf_ticker = yf.Ticker(symbol)
        self._name = symbol
        self._price = self.get_latest_price()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    def get_latest_price(self):
        latest_data = self.yf_ticker.history()
        return latest_data["Close"].iloc[-1]
