def RomanToInt(RomanNumberString):
    RomanDictionary = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,
                        "IV":4 , "IX":9  , "XL":40 , "XC":90 , "CD":400 , "CM" : 900 , "":0}
    LastRomanNumber = ""
    Integer  = 0
    for RomanNumber in RomanNumberString:
        if LastRomanNumber + RomanNumber in RomanDictionary:
            Integer =  Integer + RomanDictionary[LastRomanNumber + RomanNumber]  -  RomanDictionary[LastRomanNumber]
        else:
            Integer = Integer +RomanDictionary[RomanNumber]
        LastRomanNumber = RomanNumber
    return Integer
print(RomanToInt("MCDLXXVI"))
