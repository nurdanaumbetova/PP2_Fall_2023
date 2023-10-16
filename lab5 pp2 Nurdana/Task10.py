nums=[int(a) for a in input().split()]

def Unique(nums):
    uni=[]
    for a in nums:
        if a not in uni:
            uni.append(a)
    print(uni)
    
cn=Unique(nums) 