string = input("Enter a string to count vowels: ")
count = 0

for litter in string:
    if (litter == 'a' or 'e' or 'i' or 'o' or 'u'):
        count += 1
        print(litter)

print(f"Total vowel is {count}")
