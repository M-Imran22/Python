def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return print("Fizz Buzz")
    elif number % 5 == 0:
        return print("Buzz")
    elif number % 3 == 0:
        return print("Fizz")
    return print(number)


x = int(input("Enter a number: "))
fizz_buzz(x)
