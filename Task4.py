a=int(input())
if a%4==0 or a%400==0:
    print("YES")
elif a%100!=0:
    print("NO")
else:
    print("NO")