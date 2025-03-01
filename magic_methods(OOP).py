class Point:

    # megic methods are special methods in Python that have double underscores at the beginning and end of their names (e.g., __init__, __str__). These methods are automatically invoked by Python in specific situations

    # the __init__(self) is magic method
    def __init__(self, x, y):
        self.x = x
        self.y = y

# if we didn't define this magic method
# print(point_1 == point_2)
# will print False

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return self.x + other.x and self.y + other.y

    def draw(self):
        return f"X: {self.x} Y: {self.y}"


point_1 = Point(10, 20)
point_2 = Point(10, 20)

print(point_1 == point_2)  # now it print True
print(point_1 + point_2)
