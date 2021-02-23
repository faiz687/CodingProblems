def LongestSubsequence(arr):
    print(arr)
    LongestMemory = []
    for i in range(len(arr)):
        print("starting loop    :",arr[i])
        count = 1
        previous_number = arr[i] 
        for j in range(i+1,len(arr)):
            if arr[j] >  previous_number:
                print("starting number  : {} greater than  : {}".format(arr[j],previous_number))
                count +=1 
                previous_number  = arr[j]
        print("loop ended count is {}".format(count))
        LongestMemory.append(count)
    print(LongestMemory)
LongestSubsequence([2,4,3,7,4,5])
2,7,4,3, 8

                 





