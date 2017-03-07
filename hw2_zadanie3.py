import math


def Distance(x1, y1, x2, y2):
    '''
    Function calculates distance between points A(x1, y1) and B(x2, y2)
    '''
    sq = (x1 - x2) ** 2 + (y1 - y2) ** 2
    AB = math.sqrt(sq)
    return AB


while True:

    while True:
        try:
            Xa = float(input('Ввести координату х точки А:'))
            break
        except ValueError:
            print('Некорректный ввод. Попробуйте еще раз.')
            continue

    while True:
        try:
            Ya = float(input('Ввести координату y точки А:'))
            break
        except ValueError:
            print('Некорректный ввод. Попробуйте еще раз.')
            continue

    while True:
        try:
            Xb = float(input('Ввести координату x точки B:'))
            break
        except ValueError:
            print('Некорректный ввод. Попробуйте еще раз.')
            continue

    while True:
        try:
            Yb = float(input('Ввести координату y точки B:'))
            break
        except ValueError:
            print('Некорректный ввод. Попробуйте еще раз.')
            continue

    res = Distance(Xa, Ya, Xb, Yb)
    print('Расстояние между точками А и В = ', res)
