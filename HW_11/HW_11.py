is_continue = True

while is_continue:
    x = int(input('Enter 1st number '))
    y = int(input('Enter 2nd number '))
    action = input('Enter one of the actions + - * / ')

    if action == '+':
        res = x + y
    elif action == '-':
        res = x - y
    elif action == '*':
        res = x * y
    elif action == '/':
        if y != 0:
            res = x / y
        else:
            res = 'Division by 0 is prohibited'
    else:
        res = 'Input is not correct'
    print(x, action, y, '=', res)

    if input("Press 'y' if you want to continue calculations or other symbol to stop ") != 'y':
        is_continue = False
