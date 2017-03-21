import math

def distance(x1, y1, x2, y2):
    '''
    Function calculates distance between points A(x1, y1) and B(x2, y2)
    '''
    sq = (x1 - x2) ** 2 + (y1 - y2) ** 2
    AB = math.sqrt(sq)
    return AB


def is_year_leap(year):
    '''
    Function checks is year leap or no
    '''
    if (year != 0) and (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):
        return True
    else:
        return False


def is_triangle(a, b, c):
    '''
    Function verifies possibility of existence a triangle with sides a, b, c
    '''
    if (a + b > c) and (a + c > b) and (c + b > a):
        return True
    else:
        return False