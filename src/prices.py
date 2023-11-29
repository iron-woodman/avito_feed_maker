import random

class Price:
    stol_prices = []
    um_prices = []
    podokonnik_prices = []

    def __init__(self):
        self.stol_prices = [price for price in range(9000, 11000, 100)]
        self.um_prices = [price for price in range(20000, 22000, 100)]
        self.podokonnik_prices = [price for price in range(9000, 11000, 100)]

    def get_price(self, product: str):
        """
        получить цену товара
        :return:
        """
        if product == 'stol':
            return random.choice(self.stol_prices)
        elif product == 'um':
            return random.choice(self.um_prices)
        elif product == 'podokonnik':
            return random.choice(self.podokonnik_prices)

    def get_pod_price(self):
        """
        получить цену подоконника
        :return:
        """
        return random.choice(self.podokonnik_prices)

    def get_stol_price(self):
        """
        получить цену столешницы
        :return:
        """
        return random.choice(self.stol_prices)