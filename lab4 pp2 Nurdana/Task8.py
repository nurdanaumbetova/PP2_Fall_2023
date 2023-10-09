n=set(range(1, int(input())+1))
x=input()
while x!='HELP':
    b=set([int(i) for i in x.split()])
    a=n&b

    if len(a)>len(n)/2:
        print('YES')
        n.intersection_update(b)
    else:
        print('NO')
        n.difference_update(b)
    x=input()
print(*sorted(n, key=int))