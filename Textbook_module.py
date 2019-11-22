# Ben Lizza
# 11/20/19
# Module that will include a Person class and a Textbook that will use Person class in author

from Person_module import Person


class Textbook:
    def __init__(self, title, first, last, age, edition, isbn_number, qty_in_inventory, price):
        self.title = title
        self.author = Person(first, last, age)
        self.edition = edition
        self.isbn = isbn_number
        self.quantity = qty_in_inventory
        self.price = price

    def add_inventory(self, qty):
        self.quantity = self.quantity + qty

    def deduct_inventory(self, qty):
        if self.quantity >= qty:
            self.quantity = self.quantity - qty
            return 0
