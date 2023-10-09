student = [{input() for j in range (int(input()))} for i in range (int(input()))]
a = set.intersection(*student)
b = set.union(*student)

print(len(a), *sorted(a), x = '\n')
print(len(b), *sorted(b), x = '\n')