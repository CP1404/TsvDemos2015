__author__ = 'sci-lmw1'

numbers = list([1, 2.3, 3.1415926, -12.1])

# for number in numbers:
#     print("Format {{}} = {}!".format(number))
# for i in range(len(numbers)):
#     print("numbers[{}] = {:6}!".format(i, numbers[i]))

# print("zero padding: {:06}!".format(12.3))
    # print("Format {{:6}} = {:6}!".format(number))

# for number in numbers:
#     print("Format {{:>6}} = {:<6}!".format(number))

# name = "Ada Lovelace"
# if name.isalpha():
#     print(name.title())
# print(type(name))

things = [1, 0.2, "hi", (1, "a"), {1: 4}]
for thing in things:
    print("{:>8} is: {}".format(str(thing), type(thing)))
print("{:>8} is: {}".format(str(things), type(things)))
print(type(things))


# '"{0}" is derived from "{1}"'.format('none', 'no one')
# '"{0}" is derived from the {1} "{2}"'.format('Etymology', 'Greek', 'ethos')
# '"{0}" is derived from the {2} "{1}"'.format('December', 'decem', 'Latin')
#
# pi = 3.14159
# 'Pi rounded to {0} decimal places is {1:.2f}.'.format(2, pi)
# 'Pi rounded to 2 decimal places is 3.14.'
# 'Pi rounded to {0} decimal places is {1:.3f}.'.format(3, pi)
# 'Pi rounded to 3 decimal places is 3.142.'
# 'Pi rounded to {} decimal places is {:.3f}.'.format(3, pi)


# def printID(obj):
#     print(id(obj))
# o1 = [1, 2]
# o2 = (1, 2)
# print(id(o1))
# printID(o1)
# print(id(o2))
# printID(o2)
