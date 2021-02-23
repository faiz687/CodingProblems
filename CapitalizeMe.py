def CapitalizeMe(a):
    check = True
    newstring = ""
    for i in a:
        if check == True:
            newstring += i.upper()
            check = False
        else:
            newstring += i
        if i == " ":
            check = True
    print(newstring)
CapitalizeMe("evertything is in lower case")