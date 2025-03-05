# y = [int(x) for x in ('1', '23', '-45', '56')]

# print(y)
# print()

# x = ("1", "3", "65", "78")
# z = ("1", "3")
# y = x + z
# print(y)
# print()

# a = ("1", "3", "65", "78")
# b = (1, 3)
# c = a + b
# print(c)

# dictionory

student = {
    "name": "M Imran",
    "age": 22
}

print(student["name"])  # print name of the student.

print("Age" in student)  # print False because "Age" isn't in student dir

# Method 1:
# x = input("Enter your age: ")

# if int(x) >= 18:
#     print("You are eligible for driving.")
# else:
#     print("You aren't eligible for driving.")

# # Method 2:
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

# # Method 2: For else

# names = ["Muhammd", "Imran", "Nasir"]

# for name in names:
#     if name.startswith("S"):
#         print("Name Found.")
#         break

# else:
#     print("Name Not Found.")
