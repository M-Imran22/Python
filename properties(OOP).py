class Person:

    def __init__(self, name):
        self.__name = name  # internal private variable

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string.")
        self.__name = value

    @name.deleter
    def name(self):
        print("Deleting name...")
        del self.__name


# using the properties
person = Person("Imran")

print(person.name)  # get the name of the person

person.name = "M Imran Khan"  # call the setter and update the name

print(person.name)
# person.name = 123 # give us the TypeError "Name must be a string"

del person.name  # delete the name of a person

# print(person.name) # AttributeError because __name is gone
