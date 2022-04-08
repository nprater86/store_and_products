from uuid import uuid4

class Product():
    unique_id = 1
    def __init__(self, name, price, category):
        self.name = name
        self.id = Product.unique_id
        Product.unique_id += 1
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price *= 1 + percent_change
        else:
            self.price *= 1 - percent_change
        return self

    def print_info(self):
        print(f"ID: {self.id} | Name: {self.name} | Category: {self.category} | Price: {self.price}")
        return self