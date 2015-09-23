__author__ = 'sci-lmw1'

"""
Warm Up:
Ask the user for their name
Repeatedly re-prompt until they enter a non-empty name
Then display their name in all capitals

Algorithm

get name
while length of name == 0
    print error message
    get name
print name in all capitals

"""
#
# name = input("Name: ")
# # for i in range(0, len(name)):
# #     print(name[i])
# #
# print()

# for char in name:
#     print(char)


# phone = input("Phone: ")
# print(phone[3:])
#
text = "I'm Smith at the Smithsonian here. Are you? What!!*% $50"

new_text = text.lower()
for char in ".,/?!@#$%^&*()":
    new_text = new_text.replace(char, "")

# print(new_text)

words = new_text.split()

print("Here".lower() in words)


# def ascii(start, end):
#     output = ""
#     for i in range(start, end+1):
#         output += str(i) + " " + chr(i) + ","
#     return output
#
# print(ascii(65, 70))