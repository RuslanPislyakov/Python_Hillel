def find_unique_value(lst):
    temp_set = set(lst)

    for el in temp_set:
        if lst.count(el) == 1:
            return el
        else:
            return None


assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")
