def IsIntegerPalindrome(Number):
    if Number < 0  :
        return False 
    else:
        NumberList  = [] 
        while (Number != 0):
            Value = Number%10
            NumberList.append(Value)
            Number = Number//10
        for i in range(len(NumberList)//2):
            if  NumberList[i:i+1] != NumberList[::-1][i:i+1]:
                return False
        return True               
print(IsIntegerPalindrome(123321))

