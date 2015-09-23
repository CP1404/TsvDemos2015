__author__ = 'sci-lmw1'

""" CP1404 Week 5 - Lists, Tuples, Dictionaries """

# i = 3
# stuff = [0, "abc", [i, i * 2], True, [], 5.6]
#
# print(stuff[1], stuff[2:4], stuff[2][1])
# if stuff[4]:
#     print(stuff[:4])
# else:
#     print(stuff[4:])
# print(len(stuff))


# THRESHOLD = 20
# numbers = [1, 23, 45, -12, 9, 50]
# for number in numbers:
#     if number > THRESHOLD:
#         print(number)


# phone_numbers = ["0747739000", "0212345678", "0312345987", "0741223312"]
# qld_numbers = []
# for phone_number in phone_numbers:
#     if phone_number.startswith("07"):
#         qld_numbers.append(phone_number)
#
# qld_numbers.sort()
# print(qld_numbers)


# def filter_between(values, lower, upper):
#     results = []
#     for value in values:
#         if lower <= value <= upper:
#             results.append(value)
#     return results
#
#
my_list = [10, 2, 3, 4, 5, 6, 7, 8, 9, 12, 14, 15, 12, -12, 9, 0, 45]
# print(filter_between(my_list, 5, 10))


# def get_low_high(values):
#     return min(values), max(values)
#
# low, high = get_low_high(my_list)
# print(low, type(low))
#
# result = get_low_high(my_list)
# print(result, type(result))
#
# x, y = (1, 2)
# print(x, type(x))


# my_dob = (22, 11, 2001)
# print("I was born in", my_dob[2])
#
# date_input = input("Enter DOB (d/m/y)")
# parts = date_input.split("/") # this will be a list of strings
# my_dob = tuple([int(part) for part in parts])
# # my_dob = (int(parts[0]), int(parts[1]), int(parts[2]))
# print(my_dob)


# names = ["Bill", "Jane", "Sven"]
# ages = [21, 34, 56]
#
# i = 1
# print(names[i], "is", ages[i], "years old")


ages_dict = {"Bill": 21, "Jane": 34, "Sven": 56}
# print(ages_dict["Bill"])  # prints 21
# ages_dict["Anna"] = 98
# del ages_dict["Bill"]

name = input("Name: ")
age = int(input("age: "))
ages_dict[name] = age

for name in ages_dict:
    print(name, "\tis", ages_dict[name], "years old")

for name, age in ages_dict.items():
    print(name, "\tis", age, "years old")


# i = 2
# stuff = [0, "abc", [i, i * 2], True, [], 5.6]
#
false_values = [False, 0, 0.0, "", []]
true_values = [True, -1, 3.7, "Hello", [0]]


def printTruth(value):
    if value:
        print(value, "is True")
    else:
        print(value, "is False")

# for value in false_values + true_values:
#     printTruth(value)


# import random
# numbers = []
# length = random.randint(10, 100)
# for i in range(length):
#     number = random.randint(1, 10)
#     numbers.append(number)
# sorted_numbers = sorted(numbers)
# sorted_works = True
# for i in range(len(sorted_numbers) - 1):
#     if sorted_numbers[i] > sorted_numbers[i + 1]:
#         sorted_works = False
# print("sorted works: " + str(sorted_works))


# ages_dict = {"Bill": 21, "Jane": 34, "Sven": 56}
# name = input("Name: ")
# age = int(input("Age: "))
# ages_dict[name] = age
# for name, age in ages_dict.items():
#     print(name, "\t-\t", age,)


# def print_backwards(text):
#     for character in reversed(text):
#         print(character)
#
# print_backwards("hello")


# words = ["a", "bob", "job"]
#
#
# def format_list(values, separator='-'):
#     string = ""
#     for value in values:
#         string += str(value) + separator
#     return string[:-1]
#
# print(format_list(words))

