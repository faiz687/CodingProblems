def Removenull(s):
    finalstring = ""
    x = s.split("\n")
    for i in range(1,len(x)):
        if "NULL" in x[i].split(",") or "null" in x[i].split(","):
            del x[i]
    for i in x:
        finalstring = finalstring + i + '\n'
    print(finalstring)






Removenull("header,header\nANNUL,ANNULLED\nnull,NILL\nNULL,NULL")