def find(n):
    if 0 <= n <= 9:
        return -1

    ls = list()

    for i in range(2, 10):

        while n % i == 0:
            ls.append(i)
            n = n // i

    if n != 1:
        return -1
    s_n = 0
    while len(ls) != 0:
        s_n = s_n * 10 + ls[0]
        ls.pop(0)
    return s_n


N = int(input())

print(find(N))
