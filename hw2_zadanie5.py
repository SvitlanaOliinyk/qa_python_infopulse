def is_triangle(a, b, c):
    '''
    Function verifies possibility of existence a triangle with sides a, b, c
    '''
    if (a + b > c) and (a + c > b) and (c + b > a):
        return True
    else:
        return False


while True:
    while True:
        try:
            A = float(input('Введите сторону а: ', ))
            break
        except ValueError:
            print('Некорректный ввод. Попробуйте еще раз.')
            continue

    while True:
        try:
            B = float(input('Введите сторону b: ', ))
            break
        except ValueError:
            print('Некорректный ввод. Попробуйте еще раз.')
            continue

    while True:
        try:
            C = float(input('Введите сторону c: ', ))
            break
        except ValueError:
            print('Некорректный ввод. Попробуйте еще раз.')
            continue

    res = is_triangle(A, B, C)
    print(res)
