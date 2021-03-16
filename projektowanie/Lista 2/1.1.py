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
    x = 0
    for i in range(n):
        x = 3*x + 3
    return x

def ciag22(n):
    #element n-2 plus indeks
    x = 0
    y = 0
    z = 1
    for i in range(1, n+1):
        z = x + i
        x = y
        y = z
    return z

def ciag32(n):
    pass



def check(p, n, t1, t2):
    for i in range(p, n):
        if t1(i) == t2(i):
            print(t1(i), "=", t2(i))
        else:
            print("Mamy błąd", t1(i), "<>", t2(i))
            b1
            break
    return


#check(1, 100, ciag2, ciag22)


for i in range(2, 10):
     print(i, ciag3(i), "======")
