n=int(input())
x=''
a=set()
while x!='HELP':
    x=input()
    if x=='HELP':
        break
    p=set(x.split())
    b=input()
    if b=='YES':
        if len(a)==0:
            a=p
        else:
            a=a&p
    else:
        a-=p
print(*a)