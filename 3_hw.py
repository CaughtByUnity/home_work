def bigger_num(num1, num2):
    return max(num1, num2)

print(bigger_num(10,20))

def difference(a, b):
    if abs(a - b) == 135:
        return print('yes')
    else:
        return print('No')

difference(-135, 0)

def season(month):
    if month in (12, 1, 2):
        return print('зима')
    elif month in (3, 4, 5):
        return print('весна')
    elif month in (6, 7, 8):
        return print('лето')
    elif month in (9, 10, 11):
        return print('осень')
    else:
        return print('не является номером месяца')

season(7)

def bigger_than_ten(c, d, e):
    if c > 10 and d > 10 and e > 10:
        return print('yes')
    else:
        return print('no')

bigger_than_ten(12, 11, 17)

def amount_of_positives(some_list: list):
    amount = 0
    for n in range(5):
        if some_list[n] > 0:
            amount = amount + 1
        else:
            amount = amount + 0
    return print(amount)

amount_of_positives([-1, -10, 0, 4, 5])

def days_in_period(years: int, months: int):
    return print(29 * months + 12 * 29 * years)

days_in_period(5, 12)