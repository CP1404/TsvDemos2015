__author__ = 'sci-lmw1'

# print("Hello world")
# for i in range(10):
#     print("Thanks.")
# print("Good bye!")
#
# length = float(input("Length: "))
# width = float(input("Width: "))
# area = length * width
# cost = area * 3.5
# print("For", area, "m2 that will cost", cost)
#
# length = 8
# width = 7
# print("For", length * width, "m2 that will cost", length * width * 3.5)

# i = 0
# while i < 5:
#     j = i
#     while j < 5:
#         print(i, j)
#         j = j + 1
#     i = i + 1
#     print()

numerator = int(input("Enter a numerator: "))
denominator = int(input("Enter a denominator: "))
if denominator != 0 and numerator % denominator == 0:
    print("There is no remainder")
elif denominator != 0 and numerator % denominator != 0:
    print("There is a remainder!")
else:
    print("Error - invalid denominator")

print()
# numerator = int(input("Enter a numerator: "))
# denominator = int(input("Enter a denominator: "))
if denominator == 0:
    print("Error - invalid denominator")
elif numerator % denominator != 0:
    print("There is a remainder!")
else:
    print("There is no remainder")
