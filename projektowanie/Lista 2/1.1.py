def ciag1(n):
    if n == 0:
        return 0
    return 3 ** n + ciag1(n - 1)


def ciag2(n):
    if n == 0 or n == -1:
        return 0
    return n + ciag2(n - 2)


def ciag3(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return ciag3(n - 1) + ciag3(n - 2)



def ciag12(n):
    # x = 0
    # for i in range(n):
    #     x = 3*x + 3
    # return x
    return sum([3 ** i for i in range(1, n + 1)])

def ciag22(n):
    #element n-2 plus indeks
    # x = 0
    # y = 0
    # z = 1
    # for i in range(1, n+1):
    #     z = x + i
    #     x = y
    #     y = z
    # return z
    if not n % 2 :
        q = (n // 2 + 1)
    else:
        q = i(n + 1) // 2 + 1
    return sum([n - 2 * (i - 1) for i in range(1, q)])


def ciag32(n):
    x = (1 + 5 ** 0.5) / 2
    y = (1 - 5 ** 0.5) / 2
    return int(1 / (5 ** (1 / 2)) * (x ** n - y ** n))



def check(p, n, t1, t2):
    for i in range(p, n):
        if t1(i) == t2(i):
            print(t1(i), "=", t2(i))
        else:
            print("Mamy błąd", t1(i), "<>", t2(i))
            b1
            break
    return

