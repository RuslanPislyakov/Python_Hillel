import string

chars = string.ascii_letters

input_str = input('Enter 2 letters with a dash between ')

range_start = chars.index(input_str[0])

range_end = chars.index(input_str[2]) + 1

print(str(chars[range_start:range_end]))
