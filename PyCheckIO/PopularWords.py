# In this mission your task is to determine the popularity of certain words in the text.

# At the input of your function are given 2 arguments: the text and the array of words the popularity of which you need to determine.

# When solving this task pay attention to the following points:

# The words should be sought in all registers. This means that if you need to find a word "one" then words like "one", "One", "oNe", "ONE" etc. will do.
# The search words are always indicated in the lowercase.
# If the word wasn’t found even once, it has to be returned in the dictionary with 0 (zero) value.
# Input: The text and the search words array.

# Output: The dictionary where the search words are the keys and values are the number of times when those words are occurring in a given text.

# Precondition:
# The input text will consists of English letters in uppercase and lowercase and whitespaces.

def popular_words(text: str, words: list) -> dict:
    
    #assign outout values:
    output = {}
    text = text.lower().split("\n")
    inval = text[0]
    
    for i in text:
        text[text.index(i)] = f"{text[text.index(i)]} "
    
    for i in text[1:]:
        inval = f"{inval}{i}"
    
    inval = inval.split(" ")
    
    print(text)
    print(inval)
    
    for i in words:
        output[i] = inval.count(i)
    
    return(output)
