import pytest
from inventory import Inventory, InvalidQuantityException, NoSpaceException, ItemNotFoundException

@pytest.fixture
def no_stock_inventory():
    return Inventory(10)

@pytest.fixture
def ten_stock_inventory():
    """Returns an inventory with some test stock items"""
    inventory = Inventory(20)
    inventory.add_new_stock('Puma Shoes', 100.00, 8)
    inventory.add_new_stock('Adidas Shoes', 225.50, 2)
    return inventory

def test_add_new_stock_success(no_stock_inventory):
    no_stock_inventory.add_new_stock('Test Shoes', 10.00, 5)
    assert no_stock_inventory.total_items == 5
    assert no_stock_inventory.stocks['Test Shoes']['price'] == 10.00
    assert no_stock_inventory.stocks['Test Shoes']['quantity'] == 5

    @pytest.mark.parametrize('name,price,quantity,exception', [
        ('Test Shoes', 10.00, 0, InvalidQuantityException(
            'Cannot add a quantity of 0. Value must be at least 1 item'))
    ])

    @pytest.mark.parametrize('name,price,quantity,exception', [
        ('Test Shoes', 10.00, 0, InvalidQuantityException(
            'Cannot add a quantity of 0. Value must be at least 1 item')),
        ('Test Shoes', 10.00, 25, NoSpaceException(
            'Cannot add these 25 items. Only 10 items can be added'))
    ])

    def test_add_new_stock_bad_input(name, price, quantity, exception):
        inventory = Inventory(10)
        try:
            inventory.add_new_stock(name, price, quantity)
        except (InvalidQuantityException, NoSpaceException) as inst:
            assert isinstance(inst, type(exception)) 
            assert inst.args == exception.args
        else:
            pytest.fail("Expected error but found none")


    @pytest.mark.parametrize('name,quantity,exception,new_quantity,new_total', [
        ('Puma Test', 0,
        InvalidQuantityException(
            'Cannot remove a quantity of 0. Must remove at least 1 item'),
            0, 0),
        ('Not Here', 5,
        ItemNotFoundException(
            'Could not find Not Here in our stocks. Cannot remove non-existing stock'),
            0, 0),
        ('Puma Test', 25,
        InvalidQuantityException(
            'Cannot remove these 25 items. Only 8 items are in stock'),
        0, 0),
        ('Puma Test', 5, None, 3, 5)
    ])
