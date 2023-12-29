import keyword

var_name = input('Enter variable name ')

prohibited_chars = "!#$%&'()*+,-./:;<=>?@[\\]^`{|}~ \""
is_name_correct = True

if var_name[0].isdigit():
    is_name_correct = False

if not var_name.islower() and len(var_name) > 1:
    is_name_correct = False

for ch in prohibited_chars:
    if ch in var_name:
        is_name_correct = False

if keyword.kwlist.count(var_name) != 0:
    is_name_correct = False

print(is_name_correct)
