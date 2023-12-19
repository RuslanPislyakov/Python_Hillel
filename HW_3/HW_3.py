digit = int(input('5-digit number '))

a = str(digit % 10)
b = str(digit % 100 // 10)
c = str(digit % 1000 // 100)
d = str(digit % 10000 // 1000)
e = str(digit % 100000 // 10000)

print(a + b + c + d + e)