def SpecialString(s):
    Specialcount = len(s)
    count = 0
    while count < len(s):
        print("start :",s[count])
        for i in range(count+1,len(s)):
            print(s[count:i+1])
        count += 1
        print("next alpha")
    print("special count : {}".format(Specialcount))
SpecialString("mnonopoo")

