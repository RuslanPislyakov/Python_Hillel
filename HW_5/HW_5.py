# [1, 2, 3, 4, 5, 6] => [[1, 2, 3], [4, 5, 6]]
# [1, 2, 3] => [[1, 2], [3]]
# [1, 2, 3, 4, 5] => [[1, 2, 3], [4, 5]]
# [1] => [[1], []]
# [] => [[], []]

lst = [1, 2, 3, 4, 5, 6]
# lst = [1, 2, 3]
# lst = [1, 2, 3, 4, 5]
# lst = [1]
# lst = []

length = len(lst)
half_len = int(length / 2)

if length % 2 == 0:
    fst_part = lst[0: half_len]
    snd_part = lst[half_len: length + 1]
else:
    fst_part = lst[0: half_len + 1]
    snd_part = lst[half_len + 1: length + 1]

result = [fst_part, snd_part]
print(result)
