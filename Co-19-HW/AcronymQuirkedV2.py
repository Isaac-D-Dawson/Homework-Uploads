#AcronymQuirked.py     23.03.2020, Version 2 created 26.03.2020

# PATCH NOTES:
# V1.0: initial release.
# -Function takes strings and retuns acronyms of them.
# V2.0:
# -New function: pre_format() takes in a string and removes any special chars that would skew the output.
# -Clarified existing Logic.
# FUTURE PLANS:
# -Add in a spceific string to search for that scronyms the contents, allowing the function to apply mid-sentance.
# -Allow for functions to take in lists, to allow for processing multiple acronyms at once.
#-Allow for punctuation such as ";" in acronyms(Eg: "GL;Hf")

#At some point, i picked up that when making an acronym, if a word had three or less letters, it was lowercase.
#Recently, I've incorporated this into my typing stlye, and while it's still got some kinks (I or i?), It's a staple of me.
#This program;s functions aim to replicate that when making a 

#define our function "pre_format()"
def pre_format(value):
    #if it's a string, start operating on it.
    if isinstance(value, str) == True:
        #Firstly, Get rid of all the ",", "!", """ and "'" chars.
        #Divide it at the ","s
        strings = value.split(",")
        #Wipe Value.
        value = ""
        #glue it back together with a for loop.
        for i in strings:
            value = f"{value}{i}"
        #Repeat for all other useless chars.
        strings = value.split('"')
        value = ""
        for i in strings:
            value = F"{value}{i}"
        strings = value.split('!')
        value = ""
        for i in strings:
            value = f"{value}{i}"
        strings = value.split("'")
        value = ""
        for i in strings:
            value = f"{value}{i}"#
        #Finally, we split it on the "." chars.
        strings = value.split(".")
        #if there's only one result, we were dealing with one string, and we don't need to return a list.
        if len(strings) == 1:
            return(strings[0])
        #otherwise...
        else:
            return(strings)
    #and if it's not a string....
    else:
        #Return an error...
        print("Error: Input Value for function \"pre_format()\" not type \"string\"")
        #And return "None" so future steps of the program are less likely to choke on it.
        return(None)

#Define our function "acronym" and make it take in a value..
def acronym(value):
    #Firstly, see if we're looking at a string.
    if isinstance(value, str) == True:
        #Divide this input into individual words
        words = value.split(" ")
        #Define out output as an empty string,
        output = ""
        #For every word we have
        for i in words:
            #if it;s more than 3 letters long...
            if len(i) > 3 and len(i) != 0:
                #Append the first letter to the output, in uppercase.
                output = output + i[0].upper()
            #Otherwise, the word is more than three letters long...
            elif len(i) != 0:
                #...and it should be added to the output in lowercase.
                output = output + i[0].lower()
            else:
                #If the string is "0" chars long, we know there's something wrong. We opted out on it earlier to make sure the earlier code doesn't choke.
                output = ""
                #And return an error real quick
                print("Error: input to function \"acronym()\" empty string")
    #if it's not a string we need to return an error.
    else:
        print("Error: input to function \"acronym()\" not type \"string\"")
        #And we need to keep the program from choking anything else further down, so we set "output" to "None". We're returning the output next anyway.
        output = None
    #once we've processed the string
    return(output)

#test calls
print(acronym("This is a long string")) #"TiaLS"
print(acronym("I hope it's not an issue"))#"iHInaI". Should be "iHinaI"(?), but that can be patched next version.
#Tests to see how it handles punctuation.
print(acronym(pre_format("This is a Longer String!"))) #Returns "TiaLS"
print(acronym(pre_format("I hope it's not an issue?"))) #Returns iHinaI
#Strips it correctly, which is appropriate for a one line acronym. Might need exceptions for certain chars (GL;Hf), or for multiple acronyms in a single string, but for now it works.
#Test to see how it handles an empty string.
print(acronym(pre_format("")))          #Returns an error, but won't choke.
#Initially caused problems for the next step down, so I coded in a return error and a "None" to prevent the outer functions barfing. Wrote it into both funcs, just in case.
