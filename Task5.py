a = [int(s) for s in input().split()]
petya = int(input())
x = 1
for i in range(len(a)):
    if a[i] >= petya:
        x += 1
print(x)