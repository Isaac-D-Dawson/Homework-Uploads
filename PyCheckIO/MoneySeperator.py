#Demo code for a basic money seperator script

def money_seperator(money):
    k = 0
    outval = ""
    for i in reversed(str(money)):
                outval = f"{i}{outval}"
                if k == 2:
                    k = 0
                    outval = f" {outval}"
                else:
                    k += 1
    return(outval)

print(money_seperator(1000000))  #returns "1 000 000"

#And extended version for custom seperator chars:
def adv_money_seperator(money: int, seperator: str=" ") -> str:
    k = 0
    outval = ""
    for i in reversed(str(money)):
                outval = f"{i}{outval}"
                if k == 2:
                    k = 0
                    outval = f"{seperator}{outval}"
                else:
                    k += 1
    return(outval.strip(seperator))

print(adv_money_seperator(1000000))  #returns "1 000 000"
print(adv_money_seperator(1000000, ","))  #returns "1,000,000"

#Refactored version using modulo, with a kwarg for divisions.
def mod_money_seperator(money: int, seperator: str=" ", div: int=3) -> str:
    k = 1
    outval = ""
    for i in reversed(str(money)):
        outval = f"{i}{outval}"
        if k % div == 0:
            outval = f"{seperator}{outval}"
        k += 1
    return(outval.strip(seperator))

print("Modulo Test")
print(mod_money_seperator(1000000, ":", div=2))     #returns "1:00:00:00"
print(mod_money_seperator(1000000, ","))            #returns "1,000,000"
print(mod_money_seperator(1000000))                 #returns "1 000 000"

#Honestly, this isn't really a *money* seperator anymore, but just a general formatting tool.
#I can groove with that.

#Note to self, set new default values for genseperator, 
# come up with a better name for it, then assign some wrapper functions for money handling and time handling.

def str_money_seperator(inval: int, seperator: str=" ", split: int=3):
    return(f"{inval:,.2f}")
    #Note to self: remind myself how these string formatting things work so I make use of them.



print("str trest")
print(str_money_seperator(1000000))