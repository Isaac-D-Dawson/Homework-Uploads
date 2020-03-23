#Anagram.py     23.03.2020

def is_anagram(ana, ng):
    if sorted(ana) == sorted(ng):
        return(True)
    else:
        return(False)

print(is_anagram("", ""))
print(is_anagram("typhoon", "opython"))
print(is_anagram("Typhoon", "Opython"))     #doesn't compensate for captialiseation
print(is_anagram("Alice", "Bob"))
