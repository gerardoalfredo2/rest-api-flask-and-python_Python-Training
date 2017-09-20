class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        # Return another store, with the same name as the argument's name, plus " - franchise"
        new_store=Store(store.name+" - franchise")
        return new_store

    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
        return str(store.name)+', total stock price: '+str(store.stock_price())

store1 = Store("Test")
store2 = Store("Amazon")
store2.add_item("Keyboard", 160)
 
franq_store=Store.franchise(store1)  # returns a Store with name "Test - franchise"
franq_store2=Store.franchise(store2)  # returns a Store with name "Amazon - franchise"
 
print(Store.store_details(store1))  # returns "Test, total stock price: 0"
print(Store.store_details(store2))  # returns "Amazon, total stock price: 160"
