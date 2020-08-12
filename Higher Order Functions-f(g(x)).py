def compose(* funcs):
    def inner(data, funcs=funcs):
        result = data
        for f in reversed(funcs):
            result = f(result)
        return result
    return inner
f = eval('lambda x: ' + input())
g = eval('lambda x: ' + input())
ins = eval(input())
print(list(map(compose(f, g), ins)))