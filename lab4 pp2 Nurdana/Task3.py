a = [int(z) for z in input().split()]
b = [int(z) for z in input().split()]
numb = list(set(a) & set(b))
numb.sort()
print(*numb)