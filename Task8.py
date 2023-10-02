a=input().split()
a = [int(num) for num in a]
count=0

for i in range(len(a)):
    if i==0 or a[i]!=a[i-1]:
        count+=1

print(count)