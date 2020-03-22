#Palindrome.py      18.03.2020, finished on 22.03.2020

def palindrome(string):
    gnirts = [i for i in reversed(list(string))]
    # print(gnirts)
    # print(list(string))
    if gnirts == list(string):
        return(True)
    else:
        return(False)


print(palindrome("bob"))
print(palindrome("alice"))
print(palindrome("Aea"))
print(palindrome("aea"))
