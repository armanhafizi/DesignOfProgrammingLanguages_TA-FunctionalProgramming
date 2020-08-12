def Lucas():
    (l, r) = (2, 1)
    while True:
        (l, r) = (r, l+r)
        yield r - l
n = int(input())
ans = []
for x in Lucas():
    ans.append(int(x))
    if len(ans) == n:
        break
print(ans)