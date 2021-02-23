def LongestPalindrome(string1):
    PalindromHolder = []
    for index in range(len(string1)):
        for index2 in reversed(range(index+1)):
            if string1[index2:index+1] == string1[index2:index+1][::-1]:
                PalindromHolder.append(string1[index2:index+1])
    return(max(PalindromHolder, key = len))            
print(LongestPalindrome("uzhynqvopdbnkvu"))

