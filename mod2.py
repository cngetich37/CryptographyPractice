# use of string module
import string
# Initial list
original_list = [104, 85, 69, 354, 344, 50, 149, 65, 187, 420,
                 77, 127, 385, 318, 133, 72, 206, 236, 206, 83, 342, 206, 370]

# the list that holds the modular inverse of the number
inverse_mod_list = []
# find the mod 41 of each number
for a in original_list:
    find_modulo = a % 41
    inverse_mod_list.append(find_modulo)

# find the modular inverse of each number
for x in inverse_mod_list:
    inverse_mod = pow(x, -1, 41)
    if inverse_mod in range(1, 27):
        print(string.ascii_uppercase[inverse_mod - 1], end="")
    elif inverse_mod in range(27, 37):
        print(string.digits[inverse_mod-27], end="")
    elif inverse_mod in range(37, 38):
        print("_", end="")
