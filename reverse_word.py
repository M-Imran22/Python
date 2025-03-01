# number = int(input("Enter a number to reverse it: "))
# reverse_number = 0

# for i in range(number-1, -1, -1):


word = input("Enter somethiing to reverse it: ")
reverse_word = ""

# for i in range(len(word) - 1, -1, -1):
#     reverse_word += word[i]
# print(reverse_word)


index = len(word)-1
while index >= 0:
    reverse_word += word[index]
    index -= 1
print(reverse_word)
