def BinarySearch(arr,x):
    print("function start {}".format(arr))
    MidPoint = len(arr)//2
    print("this is mid point {}".format(MidPoint))

    if arr[MidPoint] == x:
        print("Found number {} at postion {}".format(x,arr[MidPoint]))
        return

    if MidPoint == 0:
        print("number not found {}".format(x))
        return

    if arr[MidPoint] < x:
        print("BinarySearch high {}".format(arr[MidPoint+1:]))
        BinarySearch(arr[MidPoint+1:],x)
    else:
        print("BInary Search low {}".format(arr[:MidPoint]))
        BinarySearch(arr[:MidPoint],x) 


BinarySearch([1,2,3,4,5,6],5)