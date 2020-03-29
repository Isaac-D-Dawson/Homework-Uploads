#Anagram.py     23.03.2020

#Define our function, and make it take in two stirngs. (I chose ana and ng at random from a song).
def is_anagram(ana, ng):
    #compare sorted copies of the strings. if they're equal that means the strings contain the same letters.
    if sorted(ana) == sorted(ng):
        #and if they contain the same letters in the same amounts, they're anagramable, so we return true.
        return(True)
    else:
        #if they aren't equal they aren't anagrams, so we retun false.
        return(False)

print(is_anagram("", ""))                   #Check to see how it handles empty strings. Returns True
print(is_anagram("typhoon", "opython"))     #Test to make sure the logic works. Returns True
print(is_anagram("Typhoon", "Opython"))     #doesn't compensate for captialiseation. Returns False
print(is_anagram("Alice", "Bob"))           #Two totally different strings to make sure it won't catch on a false positives.
