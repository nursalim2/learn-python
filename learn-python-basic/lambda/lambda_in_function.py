def my_func(n):
    return lambda a : a * n

mydoubler = my_func(2)
print(mydoubler(11))

mytripler = my_func(3)
print(mytripler(11))
