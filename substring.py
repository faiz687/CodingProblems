def substring(a):
    list_of_int = [0]
    alphabets = []
    count = 0
    for i in a:
        if i not in alphabets:
            alphabets.append(i)
            count += 1
        else:
            list_of_int.append(count)
            alphabets = alphabets[alphabets.index(i)+1:len(alphabets)]
            alphabets.append(i)
            count  = len(alphabets)
        list_of_int.append(count)
    return(max(list_of_int))
print(substring(a = "abcabcbb"))
