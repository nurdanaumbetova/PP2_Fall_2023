def ChikRab(heads=35,legs=94):
    for R in range(heads):
        Ch=35-R
        if ((Ch*2)+(R*4))==legs:
            return f'Chiken number = {Ch}\n Rabbit number = {R}'
       
res=ChikRab()
print(res)