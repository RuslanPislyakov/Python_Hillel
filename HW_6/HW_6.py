# lst = [12, 3, 4, 10]
# lst = [1]
# lst = []
lst = [12, 3, 4, 10, 8]

if len(lst) != 0 and len(lst) != 1:
    temp = lst.pop()
    lst.insert(0, temp)

print(lst)
