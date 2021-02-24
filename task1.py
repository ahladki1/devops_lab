N = int(input())

if N < 0:
    print("The number must be non-negative integers")
else:
    for i in range(N):
        print(i ** 2)
