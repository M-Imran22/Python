name_string = input("Enter a name to check if it's a palindrome or not. ")

name = name_string.lower()
index = len(name) - 1
reverse_name = ""
while index >= 0:
    reverse_name += name[index]
    index -= 1

if reverse_name == name:
    print(f"{name} is palindrom. {reverse_name}")
else:
    print(f"{name} isn't palindrom. {reverse_name}")
