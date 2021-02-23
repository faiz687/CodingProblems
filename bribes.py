def minimumbribes(q):
    bribes = 0 
    for i in range(len(q)):
        if q[i] - (i+1) > 2 :
            return "too chaotic"     
        for j in range(max(q[i]-2,0),i):
            if q[j] >  q[i]:
                bribes += 1
    return(bribes)
print(minimumbribes([1,2,5,3,7,8,6,4]))


