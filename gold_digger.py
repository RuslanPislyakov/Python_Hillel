import random

lst = [[7],
       [5, 8],
       [9, 8, 2],
       [1, 3, 5, 6],
       [6, 2, 4, 4, 5],
       [9, 5, 3, 5, 5, 7],
       [7, 4, 6, 4, 7, 6, 8]]

results = set()

for i in range(100):
    harvest = 0
    increment = lst[0][0]
    shift = 0

    for step in range(len(lst) - 1):

        harvest += increment

        shift += random.randint(0,1)
        increment = lst[step + 1][shift]
    harvest += increment
    results.add(harvest)

print(results)
print(max(results))
