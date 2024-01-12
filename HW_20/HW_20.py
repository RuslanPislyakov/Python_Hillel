def add_one(lst):
    k = 1
    num = 0
    res = list()

    for i in range(len(lst) - 1, -1, -1):
        num = num + lst[i] * k
        k = k * 10
    num = num + 1

    for dig in str(num):
        res.append(int(dig))

    return res


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")
