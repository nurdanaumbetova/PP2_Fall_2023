a=int(input())
b=int(input())
c=int(input())

if a<=b and a<=c:
    min=a
elif b<=a and b<=c:
    min=b
else:
    min=c

print(min)
