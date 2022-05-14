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
        def __init__(self, limit=100):
            self.limit = limit
            self.total_items = 0

    def test_custom_inventory_limit():
        """Test that we can set a custom limit"""
        inventory = Inventory(limit=25)
        assert inventory.limit == 25
        assert inventory.total_items == 0