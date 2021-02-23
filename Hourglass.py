def findhourglass(arr):
    holdinglist =  [] 
    for i in range(len(arr)-2):
        for j in range(len(arr[i])-2):
            holdinglist.append(sum(arr[i][j:j+3]) +  arr[i+1][j+1] + sum(arr[i+2][j:j+3]))
            print(holdinglist)
    return(max(holdinglist))
arr = [[1, 1, 1, 0, 0, 0], 
       [0, 1, 0, 0, 0, 0], 
       [1, 1, 1, 0, 0, 0], 
       [0, 0, 2, 4, 4, 0], 
       [0, 0, 0, 2, 0, 0], 
       [0, 0, 1, 2, 4, 0]]
print(findhourglass(arr))
