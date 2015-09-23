__author__ = 'sci-lmw1'

"""
Danielle wants to know how many selfies she will take each year
for the next 5 years if she currently takes 100 and she takes 10% more per year.

base_selfies = 100
annual_increase_rate = 0.1
current_selfies = base_selfies
for year = 1 to 5
    current_selfies = current_selfies * (1 + annual_increase_rate)
    print current_selfies
"""

base_selfies = 100
annual_increase_rate = 0.1
current_selfies = base_selfies
for year in range(1, 6):
    current_selfies = int(current_selfies * (1 + annual_increase_rate))
    print("In year", year, "you will take ", current_selfies, "selfies.")


"""
get score
if score > 90
    print “congratulations”
else if score > 50
    print “OK, I guess”
else
    print “oh…”
"""

score = float(input("Score: "))
if score > 90:
    print("congratulations")
elif score > 50:
    print("OK, I guess")
else:
    print("oh...")
