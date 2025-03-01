number = int(input("Enter a number to find the factorial: "))
orignal_number = number
factorial = 1

if number == 0:
    print("0 factoril is 0")

while number >= 1:
    factorial *= number
    number -= 1
print(f"{orignal_number} factorial is {factorial}")
