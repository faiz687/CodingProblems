def RepeatedString(s,n):
    countofa = 0
    for i in range(len(s)):
        if s[i]  == 'a':
            countofa += 1
    countofa = countofa * (n//len(s))
    finalstring = len(s) * (n//len(s))
    if finalstring < n:
        for i in s[:n - finalstring]:
            print("loooop",i)
RepeatedString("aba",10)