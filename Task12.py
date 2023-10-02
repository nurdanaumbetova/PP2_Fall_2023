a = [int(s) for s in input().split()]
k, с = [int(s) for s in input().split()]

a.append(0)
for i in range(len(a) - 1, k, -1):
    a[i] = a[i - 1]
a[k] = с
print(' '.join([str(i) for i in a]))