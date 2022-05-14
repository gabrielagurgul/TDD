import pytest

@pytest.fixture
def no_stock_inventory():
    return Inventory(10)

def test_add_new_stock_success(no_stock_inventory):
    no_stock_inventory.add_new_stock('Test Shoes', 10.00, 5)
    assert no_stock_inventory.total_items == 5
    assert no_stock_inventory.stocks['Test Shoes']['price'] == 10.00
    assert no_stock_inventory.stocks['Test Shoes']['quantity'] == 5

class Inventory:
    def __init__(self, limit=100):
        self.limit = limit
        self.total_items = 0
        self.stocks = {}

    def add_new_stock(self, name, price, quantity):
        self.stocks[name] = {
            'price': price,
            'quantity': quantity
        }
        self.total_items += quantity

 