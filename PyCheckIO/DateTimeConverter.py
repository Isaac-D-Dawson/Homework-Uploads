# Computer date and time format consists only of numbers, for example: 21.05.2018 16:30
# Humans prefer to see something like this: 21 May 2018 year, 16 hours 30 minutes
# Your task is simple - convert the input date and time from computer format into a "human" format.

# example

# Input: Date and time as a string

# Output: The same date and time, but in a more readable format

# Precondition:
# 0 < date <= 31
# 0 < month <= 12
# 0 < year <= 3000
# 0 < hours < 24
# 0 < minutes < 60

def date_time(time: str) -> str:
    
    date = time.split(" ")[0]
    clock = time.split(" ")[1]
    months = "January,Febuary,March,April,May,June,July,August,Septermber,October,November,December".split(",")
    
    date = date.split(".")
    clock = clock.split(":")
    
    if int(clock[0]) == 1:
        hours = "hour"
    else:
        hours = "hours"
    if int(clock[1]) == 1:
        minutes = "minute"
    else:
        minutes = "minutes"
    
    outval = f"{int(date[0])} {months[int(date[1])-1]} {date[2]} year {int(clock[0])} {hours} {int(clock[1])} {minutes}"
    
    #print(outval)#Debug output
    return(outval)
    
# if __name__ == '__main__':
#     print("Example:")
#     print(date_time('01.01.2000 00:00'))

#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
#     assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
#     assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
#     print("Coding complete? Click 'Check' to earn cool rewards!")
