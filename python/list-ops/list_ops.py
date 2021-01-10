def _cons(x, xs):
    return [x, *xs]


def append(xs, ys):
    return foldr(_cons, xs, ys)


def concat(lists):
    return foldl(append, lists, [])


def filter(function, xs):
    return foldr(lambda x, acc: _cons(x, acc) if function(x) else acc, xs, [])


def length(xs):
    return foldl(lambda acc, x: acc + 1, xs, 0)


def map(function, xs):
    return foldr(lambda x, acc: _cons(function(x), acc), xs, [])


def foldl(function, xs, acc):
    if len(xs) == 0:
        return acc
    x, *rxs = xs
    return foldl(function, rxs, function(acc, x))


def foldr(function, xs, acc):
    if len(xs) == 0:
        return acc
    x, *rxs = xs
    return function(x, foldr(function, rxs, acc))


def reverse(xs):
    return foldl(lambda acc, x: _cons(x, acc), xs, [])
