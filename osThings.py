"""
Demo of using import os module
Lindsay Ward, 14/10/2015
"""

import os

print(os.getcwd())
os.mkdir("temp")
os.chdir("temp")
print(os.getcwd())
os.rmdir("temp")
items = os.listdir('.')
for item in items:
    print(item)

