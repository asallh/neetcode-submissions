class StoreItem:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

    def get_name(self):
        print(self.name)

    def get_price(self):
        print(self.price)


chips = StoreItem("Chips", 1.99)  # Don't modify this line

# TODO: Access the attributes of the chips object and display them
chips.get_name()
chips.get_price()
