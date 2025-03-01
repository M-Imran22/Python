# List

# items = ["a", "b", "c"]

# print(items)

# for index, item in enumerate(items):
#     print(index)

# List Comprehension

# squre = [x**2 for x in range(10)]
# print(squre)

# Sort List

# numbers = [1, 2, 54, 7, 3, 76, 5, 6]
# numbers.sort(reverse=True)  # sort the orignal list.
# print(sorted(numbers))  # this function copy the list and sort that copy.
# print(numbers)


# Sort List of tuples

# from collections import deque
# items = [
#     ("Apple", 45),
#     ("PianApple", 42),
#     ("Orange", 12),
#     ("Banana", 67),
# ]


# def sort_item(item):
#     return item[1]


# items.sort(key=sort_item)
# print(items)

# Lamda function
# if we use a function one and pass as a perameter then we use lamda function

# items.sort(key=lambda item: item[1])
# print(items)


# Map function
# products = list(map(lambda item: item[0], items))

# print(products)


# Filtered Function
# filterd_list = list(filter(lambda item: item[1] <= 50, items))
# print(filterd_list)

# list1 = [1, 2, 4]
# list2 = [11, 32, 54]
# Zip function
# print(list(zip("imran", list1, list2)))


# Queue
# queue = deque([])
# queue.append(1)
# queue.append(2)
# queue.append(3)
# queue.popleft()
# queue.popleft()
# queue.popleft()

# if not queue:
#     print("Empty Queue")

# print(queue)

# Dictionories

# students = {
#     "name": "M Imran",
#     "Rolno": 220,
#     "Sems": 8,
# }

# print(students)
# student = dict(name="M Imran", Rolno=220, Semes=8)

# student["Department"] = "CS"
# # student["F_name"] = "Mujeeb ur Rehman"
# # print(student)

# if "College" in student:
#     print(student["College"])

# print(student.get("F_name", "F_name isn't available"))

# for key in student:
#     print(key)

# for key, value in student.items():
#     print(key, value)


# del student["Semes"]
# print(student)

# Unpacking Operator (*, **)

# numbers = [1, 2, 3, 4, 5]

# a, *b, c = numbers
# print(a)
# print(b)
# print(c)
# # print(d)

# dict1 = {"a": 1, "b": 2}
# dict2 = {"f": 5, "c": 4, "d": 10}

# combined = {**dict1, **dict2}
# print(combined)


def intro(name, age, city):
    return f"I'm {name}, {age} years old and from {city}"


person = {
    "name": "Muhammad Imran",
    "age": 22,
    "city": "Jahangira, Swabi"
}

print(intro(**person))
