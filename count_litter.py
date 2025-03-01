# string = input("Enter a string: ")
# new_string = string.lower()

# str_dict = {}

# for i in range(0, len(new_string)):
#     count = 1
#     if new_string[i] in str_dict:
#         i += 1
#     else:
#         for j in range(i+1, len(new_string)):
#             if new_string[i] == new_string[j]:
#                 count += 1
#         if i in range(0, len(new_string)):
#             str_dict[new_string[i]] = count

# This code has a few issues:
# 1. The i += 1 in the if condition doesn't affect the for loop counter
# 2. The second range check is redundant since i is already within the main loop's range
# 3. The code skips counting some characters due to the i += 1

# Here's the corrected version:
string = input("Enter a string: ")
new_string = string.lower()

str_dict = {}

for i, char in enumerate(new_string):
    # Skip if character already counted
    if char not in str_dict:
        count = 1
        for j in range(i+1, len(new_string)):
            if char == new_string[j]:
                count += 1
        str_dict[char] = count

print(str_dict)
