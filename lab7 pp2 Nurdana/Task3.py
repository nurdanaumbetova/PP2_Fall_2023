import re
file=open('row.txt', 'r', encoding="utf-8")
text = file.read()
z=re.findall('^[a-z]+_[a-z]+$', text)
print(z)

if z:
    print(z)
    print("Found")
else:
    print("Not Found")
file.close()