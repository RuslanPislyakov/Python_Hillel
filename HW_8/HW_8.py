# [1, 3, 5] => 30
# [6] => 36
# [] => 0

lst = []
result = 0

if lst:
    for i in range(0, len(lst), 2):
        result += lst[i]

    result *= lst[-1]

print(result)
