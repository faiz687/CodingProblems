def Longest_Panlindrome(s):
    if s == None or len(s) == 0 : return ""
    elif len(s) == 1 : return s[0]
    else:
        left  = (len(s)//2)-1
        right = (len(s)//2)
        while True:
            print(s[left],s[right])
            left = left-1
            right = right+1 
            print(left,right)
            input()



print(Longest_Panlindrome("aabbaa"))
