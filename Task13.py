num = input().split()
count_p = 0
for i in range(len(num)):
    for j in range(i + 1, len(num)):
        if num[i] == num[j]:
            count_p += 1

print(count_p)