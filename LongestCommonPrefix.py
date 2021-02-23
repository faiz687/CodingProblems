def LongestCommonPrefix(strs):
    if len(strs) == 0 or strs[0] == "": return ""
    if len(strs) == 1 : return strs[0]
    LongestCommonPrefix = strs[0]
    for i in range(len(strs)-1):
        print("Longest common Prefix  :  {}".format(LongestCommonPrefix))
        if LongestCommonPrefix != strs[i+1]:
            Loopcount = 0 
            if len(LongestCommonPrefix) < len(strs[i+1]):
                Loopcount  = len(LongestCommonPrefix)
            else:
                Loopcount  = len(strs[i+1])
            output = ""
            for j in range(Loopcount):
                if  strs[i+1][j] == LongestCommonPrefix[j]:
                    output += strs[i+1][j]
                else:
                    break
            LongestCommonPrefix = output
    return LongestCommonPrefix
print(LongestCommonPrefix(["a","a","a"]))