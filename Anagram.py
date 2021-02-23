def Anagram(s1,s2):
    possible_ana = {}
    deletions  = 0
    if len(s1) > len(s2):
        deletions = len(s1) - len(s2)
    elif len(s2) > len(s1):
        deletions = len(s2) - len(s1)
    for i in s1:
        if i in s2:
            if i in possible_ana:
               possible_ana[i] =  possible_ana[i] + 1
            else:
               possible_ana[i] = 1
        else:
            deletions += 1 
        print(possible_ana)
        print(deletions)
Anagram("cde","dcf")

      #"bacdc" "dcbad"