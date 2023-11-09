import re
file=open('row.txt', 'r', encoding="utf-8")
text = file.read()
z=re.sub("[ ,.]",':', text)
print(z)
file.close()