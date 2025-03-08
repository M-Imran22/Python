import random
import string

print(random.random())  # print random num between 0 to 1

print(random.randint(1, 50))  # print random num between 1 to 50

# print random num in the given list
print(random.choice([1, 2, 3, 4, 5, 6, 7]))

# print random 5 nums between in the given list.
print(random.choices([1, 2, 3, 4, 5, 6, 7], k=5))

# print random 5 chars in the given string.
print(random.choices("abcdefigh", k=5))

# generate password.

password = "".join(random.choices(string.ascii_letters + string.digits, k=8))
print("Your password is :", password)
