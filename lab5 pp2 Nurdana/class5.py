class Account():
    def __init__(x,owner,balance=0):
        x.owner=owner
        x.balance=balance
    def __str__(x):
        return f'Account owner {x.owner}/nAccount balance  {x.balance}'
    def Deposit(x,dep_b):
        x.balance+=dep_b
        print("balance topped up")
    def Withdraw(x,wd_b):
        if x.balance>=wd_b:
            x.balance-=wd_b
            print('withdraw accepted')
        else:
            print('withdraw not accepted')

  

a=int(input())
b=int(input()) 
c=str(input())          
cl=Account(c)
cl.Deposit(a)
cl.Withdraw(b)
print(cl.balance)
print(cl.owner)
