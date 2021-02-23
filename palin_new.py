def palindrome_Subs(s):
    palindrome_Words = {}
    k = ""
    if len(s) <= 1:
        return s
    else:
        for first_index,first_alpha in enumerate(s):
            if first_alpha in s[-len(s):]:
                for second_index,second_alpha in enumerate(reversed(s)):
                    if first_alpha == second_alpha:
                        k = k + second_alpha
                        if len(s) > first_index+1:
                            first_alpha = s[first_index+1]
                            first_index += 1
      
                palindrome_Words[k] = len(k)
                k = ""
        print(palindrome_Words)
        return(max(palindrome_Words,key=palindrome_Words.get))
print(palindrome_Subs("racecar"))
