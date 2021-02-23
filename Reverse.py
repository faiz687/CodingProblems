def GiveMeReverse():
    if x == 0:
        return 0
    Number = 0
    NumberString  = str(Number)
    ZeroCounter = 0
    if Number < 0:
        NumberString = NumberString[1:]
    for i in NumberString[::-1]:
        if i == "0":
            ZeroCounter = ZeroCounter + 1
        else:
            break     
    NumberStringReversed = NumberString[::-1]
    NumberStringReversed = NumberStringReversed[ZeroCounter:]
    if Number < 0:
        NumberStringReversed = "-" + NumberStringReversed
    print(NumberStringReversed)
    if int(NumberStringReversed) < -2147483648 or  int(NumberStringReversed) > 2147483648:
        return 0
    return NumberStringReversed
print(GiveMeReverse())   
GiveMeReverse()
