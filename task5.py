def diff(ls, n):
    d1 = 0
    d2 = 0

    for row in range(n):

        for column in range(n):

            if row == column:
                d1 += ls[row][column]

            if row == n - column - 1:
                d2 += ls[row][column]

    return abs(d1 - d2)


N = int(input())
lsIn = []

for a in range(N):
    s = input().split()
    for j in range(len(s)):
        s[j] = int(s[j])
    lsIn.append(s)

print(diff(lsIn, N))
