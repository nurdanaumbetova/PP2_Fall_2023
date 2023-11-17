import math
def multiply_list(numbers):
    result = math.prod(numbers)
    return result

x=[int(a) for a in input().split()]
result = multiply_list(x)

print(f"The result: {result}")
