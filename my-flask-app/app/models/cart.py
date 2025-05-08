class Cart:
    def __init__(self, id, user_id):
        self.id = id
        self.user_id = user_id
        self.items = []  # List to hold items in the cart

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def clear_cart(self):
        self.items.clear()

    def get_items(self):
        return self.items

    def total_items(self):
        return len(self.items)