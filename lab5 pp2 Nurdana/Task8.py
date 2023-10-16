list=[int(m) for m in input().split()]
def spy(list):
    list0=[]
    for a in list:
        if a==0 or a==7:
            list0.append(a)
    if list0[0]==0 and list0[1]==0 and list0[2]==7:
        print(True)
    else:
        print(False)

cn=spy(list)