__author__ = 'sci-lmw1'


class Date:
    sep = "/"

    def __init__(self, day=1, month=1, year=1970):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return "{1}{0}{2}{0}{3}".format(Date.sep, self.day, self.month, self.year)


# today = Date(10, 9, 2015)
#
# print(today)
#

