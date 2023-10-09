N,M = [int(i) for i in input().split()]
x, y = set(), set()

for i in range(N):
    x.add(int(input()))
for i in range(M):
    y.add(int(input()))
    
print(len(x & y))
print(*sorted(set(x & y)))
print(len(x - y))
print(*sorted(set(x - y)))
print(len(y - x))
print(*sorted(set(y - x)))