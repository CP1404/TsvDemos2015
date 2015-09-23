__author__ = 'sci-lmw1'

out_file = open("out.txt")
name = "Python"
age = 2
out_file.write("Python text file\n")
out_file.write("{}, {}".format(name, age))
out_file.close()

input_file = open("text.txt", 'r')
text = input_file.read()
first_line = input_file.readline()
lines = input_file.readlines()
for line in input_file:
    print(line)


# try:
#     pass #statements
# except exceptionType:
# 	statements
#

x, y = 10, 0
try:
    print(x / y)
except ZeroDivisionError:
    print("Error. Can't divide by zero!")
print("Finished")


# What are the possible outcomes for different inputs?
try:
    number = int(input("? "))
    print(10 / number)
except ValueError:
    print("Not a valid number")
except ZeroDivisionError:
    print("Can't divide by zero")
except:
    print("Some other exception happened")
print("Finished")


valid_input = False
while not valid_input:
    try:
        age = int(input("Age: "))
        valid_input = True
    except ValueError:  # or just  except:
        print("Invalid (not an integer)")
print("Next year you will be", age + 1)
