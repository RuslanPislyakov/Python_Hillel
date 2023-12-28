import random

rand_list = [random.randint(1, 10) for i in range(random.randint(3, 10))]

result_list = [rand_list[0], rand_list[2], rand_list[-2]]

print(rand_list)
print(result_list)
