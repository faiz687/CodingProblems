def MaxArraySum(arr):
    print(arr)
    MaxSets = []
    for i in range(len(arr)-2):
        firstset = sum(arr[i::2])
        # print(arr[i::2])
        secondset = sum([arr[i],sum(arr[i+3::2])])
        # print([arr[i],arr[i+3::2]])
        MaxSets.append(max(firstset,secondset))
    print(max(MaxSets))
MaxArraySum([3,5,-7,8,10]) 















