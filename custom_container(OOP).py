class ShoppingMall:

    def __init__(self):
        self.products = {}

    def add(self, product):
        self.products[product.lower()] = self.products.get(
            product.lower(), 0) + 1

    def __getitem__(self, product):
        return self.products.get(product.lower(), 0)

    def __setitem__(self, product, count):
        self.products[product.lower()] = count

    def __len__(self):
        return len(self.products)

    def __iter__(self):
        return iter(self.products)


mall = ShoppingMall()

mall.add("eggs")
# set a value to an element (key) in list
mall["eggs"] = 20

# if you add more elements (keys) of the same name, it will increase the count (value)
mall.add("Eggs")
mall.add("eggs")
mall.add("Apple")
mall.add("banana")

# get specific element (key) value from the list
print(mall["eggs"])

# print length of a list
print(len(mall))

# print all products (keys) in list
for product in mall:
    print(product)
