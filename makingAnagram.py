def PalindromeMaker(string1):
    if string1[0] == "?" or string1[0] == string1[len(string1)-1]:
        print("can be palindrome")
    else:
        print("no")
PalindromeMaker("aab??a")

