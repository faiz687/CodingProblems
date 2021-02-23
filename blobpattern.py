def substring(blob,pattern):
    Occurances = ""
    totalCount = 0 
    for i in blob:
        count = 0
        if len(pattern) > 0:
            for j in range(len(i)-len(pattern)+1):
                 if i[j:len(pattern)+j] == pattern:
                    count += 1
        Occurances = Occurances + str(count) + "|"
        totalCount = totalCount + count 
    Occurances = Occurances + str(totalCount)  
    print(Occurances)


               
substring(["bcdefbcbebc","abcdebcfgsdf","cbdbesfbcy","1bcdef23423bc32"],"aa")











