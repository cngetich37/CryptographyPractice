# import string python module
import string

Mylist = [91, 322, 57, 124, 40, 406, 272, 147, 239, 285, 353,
          272, 77, 110, 296, 262, 299, 323, 255, 337, 150, 102]

for i in Mylist:
    # find the mod 37 of each number
    new_list = i % 37
    if new_list in range(0, 26):
        # use of string to map numbers to alphabets
        print(string.ascii_uppercase[new_list], end="")
    elif new_list in range(26, 36):
        # use of string to map numbers to decimal digits
        print(string.digits[new_list-26], end="")
    elif new_list in range(36, 37):
        print("_", end="")
