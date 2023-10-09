N, K = [int(i) for i in input().split()]
a = set()
mass = [[int(i) for i in input().split()] for j in range(K)]
for i in range(K):
    d = mass[i][0]
    st = mass[i][1]
    s = mass[i][0]

    while d <= N:
        if d % 7 != 6 and d % 7 != 0:
            a.add(d)
        d += st


print(len(a))