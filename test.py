import pytest

@pytest.fixture
def no_stock_inventory():
    return Inventory(10)

def test_add_new_stock_success(no_stock_inventory):
    no_stock_inventory.add_new_stock('Test Shoes', 10.00, 5)
    assert no_stock_inventory.total_items == 5
    assert no_stock_inventory.stocks['Test Shoes']['price'] == 10.00
    assert no_stock_inventory.stocks['Test Shoes']['quantity'] == 5

class InvalidQuantityException(Exception):
        pass

class Inventory:
    def __init__(self, limit=100):
        self.limit = limit
        self.total_items = 0
        self.stocks = {}

    def add_new_stock(self, name, price, quantity):
        if quantity <= 0:
            raise InvalidQuantityException(
                'Cannot add a quantity of {}. Value must be at least 1'.format(quantity))
        self.stocks[name] = {
            'price': price,
            'quantity': quantity
        }
        self.total_items += quantity

    @pytest.mark.parametrize('name,price,quantity,exception', [
    ('Test Shoes', 10.00, 0, InvalidQuantityException(
        'Cannot add a quantity of 0. Value must be at least 1'))
    ])
    def test_add_new_stock_bad_input(name, price, quantity, exception):
        inventory = Inventory(10)
        try:
            inventory.add_new_stock(name, price, quantity)
        except InvalidQuantityException as inst:
            assert isinstance(inst, type(exception))
            assert inst.args == exception.args
        else:
            pytest.fail("Expected error but found none")


   

    
