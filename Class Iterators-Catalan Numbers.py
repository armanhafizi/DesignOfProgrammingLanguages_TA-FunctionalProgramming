import scipy.special
class Catalan():
    def __init__(self):
        self.n = 1
    def __next__(self):
        (self.n, k) = (self.n + 1, self.n)
        return (scipy.special.binom(2*k, k) / (k + 1))
    def __iter__(self):
        return self
n = int(input())
ans = []
for x in Catalan():
    ans.append(int(x))
    if len(ans) == n:
        break
print(ans)