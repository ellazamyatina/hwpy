def _curry_call(fn, n, args):
    if n < 0:
        raise Exception("Arity passed is negative")

    if len(args) == n:
        try:
            return fn(*args)
        except TypeError as e:
            if "positional argument" in str(e):
                raise Exception("Incorrect amount of arguments passed to curry")
            raise e
    elif len(args) < n:
        return lambda x: _curry_call(fn, n, args + [x])
    else:
        raise Exception("Implementation error")


def curry(fn, n):
    return _curry_call(fn, n, [])


def uncurry(fn, n):
    if n < 0:
        raise Exception("Arity passed is negative")

    def _inner(*args):
        if len(args) != n:
            raise Exception("Wrong argument number")
        cur = fn(args[0])
        for i in range(1, n):
            cur = cur(args[i])
            if not callable(cur) and i != n - 1:
                raise Exception("Incorrect number of arguments passed to uncurry")
        return cur

    return _inner


def sum(a, b, c):
    print(a, b, c)
    return a + b + c


curried_sum = curry(sum, 4)
print(curried_sum(1)(2)(3))
