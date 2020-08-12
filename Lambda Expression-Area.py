def area(t):
    return (t[0] * t[1])/2.0
inp = eval(input())
ans = list(map(area, filter(lambda t: t[0]**2 + t[1]**2 == t[2]**2, inp)))
print(ans)