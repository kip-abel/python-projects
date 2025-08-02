class CoffeeMenu:
    def __init__(self):
        self.menu ={
            'espresso': 2.50,
            'latte': 2.75,
            'cappuccino': 3.20,
            'americano': 2.70
        }

    def get_price(self, item):
        return self.menu.get(item, None)

    def add_item(self, item, price):
        if price <= 0:
            raise ValueError("Price must be positive")
        self.menu[item] = price