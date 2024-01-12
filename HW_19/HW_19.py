import random


def common_elements():
    list_1 = [random.randrange(0, 50, 3) for i in range(random.randint(3, 20))]
    list_2 = [random.randrange(0, 50, 5) for i in range(random.randint(3, 20))]

    set_1 = set(list_1)
    set_2 = set(list_2)

    print('Random list 1: ', list_1)
    print('Set 1: ', set_1)
    print('Random list 2: ', list_2)
    print('Set 1: ', set_2)

    res = set_1.intersection(set_2)
    if res:
        return res
    else:
        return None


print('Result: ', common_elements())
