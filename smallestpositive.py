def smallpnum(a):
    biggest = max(a)
    if biggest <= 0:
        return 1
    else:
        for i in range(biggest):
            if i+1 not in a:
                return i+1
        return biggest + 1
print(smallpnum([-1,-3],))