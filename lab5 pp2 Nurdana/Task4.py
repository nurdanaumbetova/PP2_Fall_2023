nums=[int(a) for a in input().split()]

def filter_prime(nums):
    prime=[]
    for i in nums:
        bool=True
        if i<=1:
            bool=False
        for x in range(2,i-1):
            if i%x==0:
                bool=False
        if bool==True:
            prime.append(i)
    return prime
                
cn=filter_prime(nums)
print(f'Prime numbers are: {cn}')