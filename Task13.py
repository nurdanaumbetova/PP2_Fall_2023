a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a > b:
    a, b = b, a
if c >= a / 2:
    c = a - c
if d >= b / 2:
    d = b - d

if c < d:
    print(c)
else:
    print(d)