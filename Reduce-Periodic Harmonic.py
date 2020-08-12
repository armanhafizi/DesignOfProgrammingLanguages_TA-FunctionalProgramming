import functools
def Harmonic(x, y):
    return x + ((-1)**(y+1))*(1/y)
n = int(input())
s = functools.reduce(Harmonic, range(1,n+1))
print('%.3f' % s)