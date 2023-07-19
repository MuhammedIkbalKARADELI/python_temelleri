def fonk(x):
    res = 0
    i = 1
    while i < x:
        res = res + (i*(i+1))
        i = i+1
    
    return res

print(fonk(4))

