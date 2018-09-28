def fib_1(i):
    if i == 0:
        return 1
    elif i == 1:
        return 1
    else:
        return fib_1(i - 1) + fib_1(i - 2)

def fib_1_mem(i, m={}):
    if i in m:
        return m[i]['val']
    else:
        computed_val = None
        if i == 0:
            computed_val = 1
        elif i == 1:
            computed_val = 1
        else:
            computed_val = fib_1_mem(i - 1, m) + fib_1_mem(i - 2, m)
        m[i] = {'val': computed_val}
        return computed_val


def fib_2(i):
    last = 1
    cur = 1
    for n in range(0, i - 1):
        next_fib = cur + last
        last = cur
        cur = next_fib
    return cur

