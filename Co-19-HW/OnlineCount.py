#OnlineCount.py     18.03.2020

#test data
statuses = {"Alice":"online", "Bob":"offline", "Candice":"offline", "Dave": "online", "Eve":"online", "online":"ofline"}

#Define our function and make it take in a dictionary.
def online_count(dictionary):
    #Allocate online and set it to 0.
    online = 0
    #Cycle through everything in the dictionary...
    for i in dictionary:
        #And if each item in the dictionary has the value "online"
        if dictionary[i].lower() == "online":
            #Add it to the output
            online += 1
    #Finally, return the total.
    return(online)

#Test call
print(online_count(statuses))   #Returns 3.