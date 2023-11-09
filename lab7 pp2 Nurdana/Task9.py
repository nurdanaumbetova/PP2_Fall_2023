import re
file=open('row.txt', 'r', encoding="utf-8")
text = file.read()
z=re.sub(r"(\w)([A-Z])", r"\1 \2", text)
print(z)
file.close()