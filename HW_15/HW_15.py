init_digit = int(input('Enter the amount of seconds from 1 to 8640000: '))

days, seconds = divmod(init_digit, 24 * 60 * 60)
hours, seconds = divmod(seconds, 60 * 60)
minutes, seconds = divmod(seconds, 60)

print(f"{days} днів, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
