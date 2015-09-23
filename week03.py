__author__ = 'sci-lmw1'

i = 5
j = 12

# print(i, j, sep="")
#
# salary = 35789
#
# print("Your salary is: ", end="")
# print("$", salary, j, i, sep="")

# start = 5
# end = 50
# step = 3
#
# for i in range(start, end+1, step):
#     print(i, end=", ")
#     i = i + 1000
#     print(i)

# start_year = int(input("Start year: "))
# end_year = int(input("End year: "))
# start_year = 1996
# end_year = 2015
# for year in range(start_year, end_year+1, 4):
#     # print(year)
#     # for char in str(year):
#     year_string = str(year)
#     for i in range(3):
#         print(year_string[i], end="-")
#     print(year_string[3])

# pow(3, 4, 5, 6)

# name = "Lindsay"
#
#
#
# def repeat_string(string, number):
#     if True:
#         return string * number
#     return "No"
#
# print(repeat_string(12, 5))
#
# print(name)
#
# print(print("Hi"))


age = int(input("Age: "))
# while age > 120 or age < 0:
while not (120 >= age >= 0):
    print("Wrong!")
    age = int(input("Age: "))

print("you are", age, "years old")
