def greeting(name: str) -> str:
    return f"Welcome {name} to Python course."


print(greeting("Muhammad Imran"))


def multiply_number(number: int, multiple_by: int) -> int:
    result = number * multiple_by
    return result


x = int(input("Enter a number: "))
y = int(input("Multiple by: "))
print(multiply_number(x, y))

# Give us a list


def add_numbers(list):
    return print(list)


add_numbers([2, 3, 4, 5])

# Give us a tuple


# def add_numbers(*list):
#     return print(list)


# add_numbers(2, 3, 4, 5)


# def add_numbers(*list):
#     totle = 0
#     for number in list:
#         totle += number
#     return totle


# print(add_numbers(1, 2, 3, 4, 5))

# Give us a dictionory


def save_car(**car):
    return print(car, "\n", car["name"])


save_car(id=1, name="BMW")
