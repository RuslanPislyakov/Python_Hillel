init_digit = int(input('Enter the amount of seconds from 1 to 8640000: '))

days, seconds = divmod(init_digit, 24 * 60 * 60)
hours, seconds = divmod(seconds, 60 * 60)
minutes, seconds = divmod(seconds, 60)

if 11 <= days <= 14:
    day_print_form = 'днів'
elif 2 <= days % 10 <= 4:
    day_print_form = 'дні'Added different day string forms depending on the day amount
elif days % 10 == 1:
    day_print_form = 'день'
else:
    day_print_form = 'днів'

print(f"{days} {day_print_form}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")

