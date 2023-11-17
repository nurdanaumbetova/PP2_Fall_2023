import time
def sqTime(s,m):
    time.sleep(m/1000)
    return (s**0.5)

s=int(input("Enter second: "))
m=int(input('Enter msecond: '))
d=sqTime(s,m)
print(f'Square root of {s} after {m} miliseconds is {d}')