def duplicate(s,arr):
    cost = 0
    for i in range(len(s)-1):
        print(s[i],s[i+1])
        if s[i] == s[i+1]:
            print("equal cost :",arr[i] , arr[i+1])
            if arr[i] <= arr[i+1]:
                cost = cost + arr[i]
            else:
                cost = cost + arr[i+1]
duplicate("ababa",[10,5,10,5,10])