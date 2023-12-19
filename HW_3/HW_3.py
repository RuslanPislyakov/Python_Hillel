digit = int(input('5-digit number '))

a = digit % 10
b = digit % 100 // 10
c = digit % 1000 // 100
d = digit % 10000 // 1000
e = digit % 100000 // 10000

result = a * 10000 + b * 1000 + c * 100 + d * 10 + e

print(result)