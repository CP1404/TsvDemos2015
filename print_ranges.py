"""
A simple function for computing and printing the the ranges of points
given a maximum points value of Pass, Credit, and HD levels
"""

__author__ = 'Jason'


def print_ranges(maximum_value):
    results = [("P", 0.5 * maximum_value, 0.64 * maximum_value),
               ("C", 0.65 * maximum_value, 0.74 * maximum_value),
               ("D", 0.75 * maximum_value, 0.84 * maximum_value),
               ("HD", 0.85 * maximum_value, maximum_value)]

    print("ranges (maximum value: {})".format(maximum_value))
    for result in results:
        grade, min_value, max_value = result
        print("{:3} {:5.2f} - {:7.2f}".format(grade, min_value, max_value))
    print()


# examples
print_ranges(100)
print_ranges(30)
