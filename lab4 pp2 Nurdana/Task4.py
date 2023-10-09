numb = list(input().split())
x = set()
for i in numb:
    if i in x:
        print("YES")
    else:
        print("NO")
    x.add(i)