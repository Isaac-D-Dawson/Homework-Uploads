#OnlineCount.py     18.03.2020

#test data
statuses = {"Alice":"online", "Bob":"offline", "Candice":"offline", "Dave": "online", "Eve":"online"}

def online_count(dictionary):
    online = 0
    for i in dictionary:
        if dictionary[i].lower() == "online":
            online += 1
    return(online)

print(online_count(statuses))
