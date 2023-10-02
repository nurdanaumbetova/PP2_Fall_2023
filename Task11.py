a = input().split()
x=int(input())

for i in range(x, len(a)-1):
    a[i]=int(a[i])
    a[i]=a[i+1]
a.pop()

for i in range(len(a)):
    print(a[i])