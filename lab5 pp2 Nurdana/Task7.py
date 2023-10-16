def has33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

nums = input().split()
nums = [int(i) for i in nums]  

res = has33(nums)
print(res)

