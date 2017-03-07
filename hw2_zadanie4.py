def is_year_leap(year):
    '''
    Function checks is year leap or no
    '''
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        return True
    else:
        return False


while True:
    try:
        year_in = int(input('Введите год: ', ))
        break
    except ValueError:
        print('Некорректный ввод. Попробуйте еще раз.')
        continue

res = is_year_leap(year_in)
print(res)
