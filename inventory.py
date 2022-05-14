class InvalidQuantityException(Exception):
        pass

class NoSpaceException(Exception):
        pass 

class ItemNotFoundException(Exception):
    pass

def test_buy_and_sell_nikes_adidas():
    
    inventory = Inventory()
    assert inventory.limit == 100
    assert inventory.total_items == 0

    # Add new Nike sneakers
    inventory.add_new_stock('Nike Sneakers', 50.00, 10)
    assert inventory.total_items == 10

    # Add new Adidas sneakers
    inventory.add_new_stock('Adidas Sneakers', 70.00, 5)
    assert inventory.total_items == 15

    # Remove 2 sneakers to sell
    inventory.remove_stock('Nike Sneakers', 2)
    assert inventory.total_items == 13

    # Remove 1 shoeas to sell
    inventory.remove_stock('Adidas Sneakers', 1)
    assert inventory.total_items == 12

    def test_default_inventory():
        """Test that the default limit is 100"""
        inventory = Inventory()
        assert inventory.limit == 100
        assert inventory.total_items == 0

class Inventory:

    def test_custom_inventory_limit():
        """Test that we can set a custom limit"""
        inventory = Inventory(limit=25)
        assert inventory.limit == 25
        assert inventory.total_items == 0

    def __init__(self, limit=100):
        self.limit = limit
        self.total_items = 0
        self.stocks = {}

    def add_new_stock(self, name, price, quantity): 
        if quantity <= 0:
            raise InvalidQuantityException(
                'Cannot add a quantity of {}. All new stocks must have at least 1 item'.format(quantity))
        if self.total_items + quantity > self.limit:
            remaining_space = self.limit - self.total_items
            raise NoSpaceException(
                'Cannot add these {} items. Only {} more items can be stored'.format(quantity, remaining_space))
        self.stocks[name] = {
            'price': price,
            'quantity': quantity
        }
        self.total_items += quantity

    def remove_stock(self, name, quantity):
        
        if quantity <= 0:
            raise InvalidQuantityException(
                'Cannot remove a quantity of {}. Must remove at least 1 item'.format(quantity))
        if name not in self.stocks:
            raise ItemNotFoundException(
                'Could not find {} in our stocks. Cannot remove non-existing stock'.format(name))
        if self.stocks[name]['quantity'] - quantity <= 0:
            raise InvalidQuantityException(
                'Cannot remove these {} items. Only {} items are in stock'.format(
                    quantity, self.stocks[name]['quantity']))
        self.stocks[name]['quantity'] -= quantity
        self.total_items -= quantity
    