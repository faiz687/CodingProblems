def MinimumSwipes(a):
    swipes = 0
    lopy  =  False
    while not lopy:
        count = 0
        for i in range(len(a)):
            if a[i] == i+1:
                count += 1
                if count >= len(a):
                    lopy = True
                continue 
            if  a[a[i]-1] - (i+1)  <=  a[a[i]-1] - a[i-1]:
                hold      =  a[i]
                a[i]      =  a[a[i]-1]
                a[hold-1] =  hold
                swipes += 1
    return swipes
print(MinimumSwipes([1,3,5,2,4,6,7]))




