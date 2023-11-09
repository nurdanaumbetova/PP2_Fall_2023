import re
def to_camel(text):
    return re.sub(r'_([a-z])', lambda x: x.group(1).upper(), text)

text=str(input("Enter the text: "))
print(to_camel(text)) 