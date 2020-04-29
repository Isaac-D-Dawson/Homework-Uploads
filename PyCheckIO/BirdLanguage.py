# Stephan has a friend who happens to be a little mechbird. Recently, he was trying to teach it how to speak basic language. Today the bird spoke its first word: "hieeelalaooo". This sounds a lot like "hello", but with too many vowels. Stephan asked Nikola for help and he helped to examine how the bird changes words. With the information they discovered, we should help them to make a translation module.

# The bird converts words by two rules:
# - after each consonant letter the bird appends a random vowel letter (l ⇒ la or le);
# - after each vowel letter the bird appends two of the same letter (a ⇒ aaa);
# Vowels letters == "aeiouy".

# You are given an ornithological phrase as several words which are separated by white-spaces (each pair of words by one whitespace). The bird does not know how to punctuate its phrases and only speaks words as letters. All words are given in lowercase. You should translate this phrase from the bird language to something more understandable.

# Input: A bird phrase as a string.

# Output: The translation as a string.

# Precondition: re.match("\A([a-z]+\ ?)+(?<!\ )\Z", phrase)
# A phrase always has the translation.

VOWELS = "aeiouy"

def translate(phrase):
    
    #Create local variables:
    vowels = "a,e,i,o,u,y".split(",")
    invals = phrase.split(" ")#seperate into words, and we'll glue it back together after.
    output = ""
    
    #iterate through our input
    #We can't iterate normally as we have to skip certain letters...
    #So lets use a while loop with an incremimentor
    global i
    for j in invals:
        i = 0
        while i <= len(j)-1:
            if j[i] in vowels:
                output = f"{output}{j[i]}"
                i += 2 #Add two, as we add one at the end, making it the three extra letters for the vowel.
            elif j[i] not in vowels:
                output = f"{output}{j[i]}"
                i += 1
            else:
                output = f"{output}{j[i]}"
            i += 1
        output = f"{output} "
        
    
    print(output[0:-1])
    return(output[0:-1])
    
# if __name__ == '__main__':
#     print("Example:")
#     print(translate("hieeelalaooo"))

#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert translate("hieeelalaooo") == "hello", "Hi!"
#     assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
#     assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
#     assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
#     print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
