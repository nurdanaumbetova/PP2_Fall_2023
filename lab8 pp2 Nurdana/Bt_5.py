def true(t):
    return all(t)

my_tuple = (True, True, False, True)

if true(my_tuple):
    print("All elements are True.")
else:
    print("Not all elements are True.")