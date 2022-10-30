import cmath


def equation():
    y = float(input())
    print('y = {}'.format(y))
    if y >= 0:
        print('x = ''%0.3f' % (y ** 0.5 + 1))
    else:
        print('x = {}'.format(cmath.sqrt(y) + 1))

equation()