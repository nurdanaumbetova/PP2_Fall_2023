n=int(input())
hour=n//60
while(hour>23):
    hour=hour-24

print(hour,n%60)