# y = [int(x) for x in ('1', '23', '-45', '56')]

# print(y)

# x = ("1", "3", "65", "78")
# z = ("1", "3")
# y = x + z
# print(y)


# a = ("1", "3", "65", "78")
# b = (1, 3)
# c = a + b
# print(c)

# dictionory

# student = {
#     "name": "M Imran",
#     "age": 22
# }

# # print(student["name"])
# print("Age" in student)


# x = input("Enter your age: ")

# if int(x) >= 18:
#     print("You are eligible for driving.")
# else:
#     print("You aren't eligible for driving.")


# message = "Eligible" if int(x) > 18 else "Not eligible"
# print(message)

# Method 1:

# names = ["Muhammd", "Imran", "Nasir"]
# found = False

# for name in names:
#     if name.startswith("I"):
#         print("Name Found.")
#         found = True

# if not found:
#     print("Name Not Found.")

# Method 2: For else

names = ["Muhammd", "AImran", "Nasir"]

for name in names:
    if name.startswith("I"):
        print("Name Found.")
        break

else:
    print("Name Not Found.")
