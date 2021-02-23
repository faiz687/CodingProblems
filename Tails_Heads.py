def tailheads(arr):
    count    = 1
    arr1     = arr[:]
    arr2     = arr[:]
    changes1 = 0
    changes2 = 0
    while count < len(arr):
        if arr1[count] == arr1[count - 1]:
            changes1 += 1
            if arr1[count -1 ] == 1:
                arr1[count] = 0
            else :
                arr1[count] = 1
        count += 1

    count = len(arr2)-1
    while count >= 0:
        if arr2[count] == arr2[count - 1]:
            changes2 += 1
            if arr2[count - 1 ] == 1:
                arr2[count] = 0
            else :
                arr2[count] = 1
        count -= 1
    print(changes1,changes2)
    return(min(changes1,changes2))








             







