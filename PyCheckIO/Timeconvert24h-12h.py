# You prefer a good old 12-hour time format. But the modern world we live in would rather use the 24-hour format and you see it everywhere. Your task is to convert the time from the 24-h format into 12-h format by following the next rules:
# - the output format should be 'hh:mm a.m.' (for hours before midday) or 'hh:mm p.m.' (for hours after midday)
# - if hours is less than 10 - don't write a '0' before it. For example: '9:05 a.m.'
# Here you can find some useful information about the 12-hour format:
# https://en.wikipedia.org/wiki/12-hour_clock

# Input: Time in a 24-hour format (as a string).

# Output: Time in a 12-hour format (as a string).

# Precondition:
# '00:00' <= time <= '23:59'

def time_converter(time):
    
    #Create ,local variables
    inval = int(time[0:2])
    half = "a"
    #If it's noon.
    if inval == 12:
        #Append the P for "12 pm"
        half = "p"
    #if it's after noon
    if inval > 12:
        #Get the 12 hour time
        inval -= 12
        #Append the p.
        half = "p"
    #if it's midnight
    if inval == 0:
        #Set to "12...
        inval = 12
        #..am"
    
    #Finally reformat as a time
    outval = f"{inval}{time[2:]} {half}.m."
    
    #print(outval)
    return(outval)
    
# if __name__ == '__main__':
#     print("Example:")
#     print(time_converter('12:30'))

#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert time_converter('12:30') == '12:30 p.m.'
#     assert time_converter('09:00') == '9:00 a.m.'
#     assert time_converter('23:15') == '11:15 p.m.'
#     print("Coding complete? Click 'Check' to earn cool rewards!")
