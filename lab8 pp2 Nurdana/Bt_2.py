def upper_lower(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())

    return upper_count, lower_count

str=input()
upper, lower = upper_lower(str)

print(f"Uppercase: {upper}")
print(f"Lowercase: {lower}")
