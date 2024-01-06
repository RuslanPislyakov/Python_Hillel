init_digit = input('Enter the digit to operate ')

multiplication_result = 1

while True:
    for el in init_digit:
        multiplication_result *= int(el)

    init_digit = str(multiplication_result)

    if multiplication_result <= 9:
        break

    multiplication_result = 1
print('Operations result: ', multiplication_result)
