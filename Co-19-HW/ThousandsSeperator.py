#ThousandsSeperator.py      23.03.2020

#Define our function and make it take a number as input.
def format_number(num):
    #Reverse the number to get the number backwards as a string.
    mun = list(reversed(str(num)))
    #create a value called offset and save it as 0.
    offset = 0
    #For every thrid number between 3 and the number of digits in our input...
    for i in range(3, (len(str(num))), 3):
        #print(mun) Testcode
        #add a comma to the number, at the current place plus the offset.
        mun.insert(i+offset, ",")
        #print(mun) Also test code
        #Then increase the offset by one.
        offset += 1
        #The offset ensures that we don't ignore the "," we just put in when putting the next one in.
    #Save the result as a reversed copy of our edited list. we reversed it twice, so now it's the right way around.
    result = list(reversed(mun))
    #Save the output as an empty string.
    out = ""
    #Cycle through every digit in the result...
    for i in result:
        #and place them in the out string.
        out = out + i
    #finally, Return Out.
    return(out)

#Test code
print(format_number(10))            #Returns 10
print(format_number(100))           #Returns 100
print(format_number(1000))          #Returns 1,000
print(format_number(10000))         #Returns 10,000
print(format_number(100000))        #Returns 100,000
print(format_number(1000000))       #Returns 1,000,000
print(format_number(10000000))      #Returns 10,000,000
print(format_number(100000000))     #Returns 100,000,000
print(format_number(1000000000))    #Returns 1,000,000,000
print(format_number(10000000000))   #Returns 10,000,000,000
print(format_number(100000000000))  #Returns 100,000,000,000
