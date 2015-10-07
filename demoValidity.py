"""
CP1404 example - ckecking valid numbers
"""
__author__ = 'Lindsay Ward'
def get_valid_number(lower, upper):
    valid = (False)
    while not valid:
        try:
            x = int(input("Enter number: "))
            if x < lower or x> upper:
                print("Number is out of range")
        except:
            print("Number is bad")
    return x

# test
age = get_valid_number(0, 120)
print("You are",age,"years old")
    print("Finished")