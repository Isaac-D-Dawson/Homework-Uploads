#AcronymQuirked.py     23.03.2020

#Define out function "acronym" and make it take in strings.
def acronym(string):
    #Divide this input into individual words
    words = string.split(" ")
    #Need to find a way to clear out special characters so they don't count. Might write a wrapper function for that.
    #Define out output as an empty string,
    output = ""
    #For every word we have
    for i in targets:
        #if it;s more than 3 letters long(currently includes "'" chars >.<)...
        if len(i) > 3:
            #Append the first letter to the output, in lowercase.
            output = output + i[0].lower()
        #Otherwise, the word is more than three letters long...
        else:
            #...and it should be added to the output in uppercase.
            output = output + i[0].upper()
    #once we've done all the words, return the acronym to whoever called the function.
    return(output)

#test calls
print(acronym("This is a long string")) #"TiaLS"
print(acronym("I hope it's not an issue"))#"iHInaI". Should be "IHinaI", but that can be patched next version.
