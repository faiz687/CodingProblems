def TripleSum(a,b,c):
    connections = {}
    for i in range(len(b)):
        if b[i] in connections:
            continue
        for j in range(b[i]+1):
            if j in c:
                if b[i] in connections:
                    connections[b[i]] = connections[b[i]] + 1
                else:
                    connections[b[i]] =  1
    triplets = 0
    for i in range(len(a)):
        for j in connections:
            if  a[i] <= j:
                triplets += connections[j]
    return triplets

print(TripleSum([1,4,5],[2,3,3],[1,2,3]))
