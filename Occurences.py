def Occurences(s):
    if len(s) <= 1:
        return True
    else:
        for i in range(len(s)):
            if s[i] == "b":
                if 'a' in s[i:len(s)]:
                    return False
        return True
print(Occurences("a"))
