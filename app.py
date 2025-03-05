import math
x = 2
y = 35
result = x * y
print(result)

# String

first = "Muhammad"
last = "Imran"
# full = first + " " + last
full = f"{first}, age: {20+2}"
print(full)


# String Methods

collage_name = "   GDC Lahor"
print(collage_name)
print(collage_name.upper())
print(collage_name.lower())
print(collage_name.count(''))
print(collage_name.strip())
print(collage_name.title())
print(collage_name.find("La"))  # give and index of the litter.
print(collage_name.replace("a", "x"))
print("D" in collage_name)  # give us a boolean value.

# Numbers

print(11 + 4)
print(11 - 4)
print(11 * 4)
print(11 / 4)  # give us the flooting point number
print(11 // 4)  # give us the int number
print(11 % 4)
print(11 ** 4)  # 11 power 4
x = 30
print(x)
x += 5
print(x)

# More in Numbers


print(round(2.4))
print(abs(-5.8))
print(math.floor(48.9))
print(round(math.sqrt(10)))
print(math.cbrt(91))
print(math.factorial(6))
