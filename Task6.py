a=input().split()
a = [int(num) for num in a]
max=a[0]
maxi=0
for i in range(len(a)):
    if(a[i]>max):
        max=a[i]
        maxi=i

print(max)
print(maxi)