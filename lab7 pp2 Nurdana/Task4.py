import re
file=open('row.txt', 'r', encoding="utf-8")
text = file.read()
z=re.findall('[A-Z]+[a-z]+', text)

if z:
    print(z)
    print("Found")
else:
    print("Not Found")
file.close()