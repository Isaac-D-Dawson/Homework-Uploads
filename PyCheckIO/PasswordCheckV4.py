# In this mission you need to create a password verification function.

# Those are the verification conditions:

# the length should be bigger than 6;
# should contain at least one digit, but it cannot consist of just digits;
# having numbers or containing just numbers does not apply to the password longer than 9.
# Input: A string.

# Output: A bool.

#I...What. This includes ALL code from versions 3 down...I don't even know anymore.

# # Taken from mission Acceptable Password III

# # Taken from mission Acceptable Password II

# # Taken from mission Acceptable Password I

# def is_acceptable_password(password: str) -> bool:
#     if len(password) > 6:
#         return(True)
#     else:
#         return(False)


# if __name__ == '__main__':
#     print("Example:")
#     print(is_acceptable_password('short'))

#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert is_acceptable_password('short') == False
#     assert is_acceptable_password('muchlonger') == True
#     assert is_acceptable_password('ashort') == False
#     print("Coding complete? Click 'Check' to earn cool rewards!")


# def is_acceptable_password(password: str) -> bool:
    
#     numbers = range(1, 10)
#     output = False
    
#     for i in numbers:
#         if str(i) in password:
#             output = True
        
#         if len(password) <=6:
#             output = False
    
#     return(output)

# if __name__ == '__main__':
#     print("Example:")
#     print(is_acceptable_password('short'))

#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert is_acceptable_password('short') == False
#     assert is_acceptable_password('muchlonger') == False
#     assert is_acceptable_password('ashort') == False
#     assert is_acceptable_password('muchlonger5') == True
#     assert is_acceptable_password('sh5') == False
#     print("Coding complete? Click 'Check' to earn cool rewards!")


# def is_acceptable_password(password: str) -> bool:
    
#     numbers = "0,1,2,3,4,5,6,7,8,9".split(",")
#     letters = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z".split(",")
#     global output
#     output = False
#     number = False
#     letter = False
    
#     for i in numbers:
#         if i in password:
#             number = True
#     for i in letters:
#         if i in password:
#             letter = True
#     if letter == True and number == True:
#         if len(password) <= 6:
#             output = False
#         else:
#             output = True
#     #print(f"Letter={letter}")
#     #print(f"number={number}")
#     #print(f"output={output}")
#     return(output)


# if __name__ == '__main__':
#     print("Example:")
#     print(is_acceptable_password('short'))

#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert is_acceptable_password('short') == False
#     assert is_acceptable_password('muchlonger') == False
#     assert is_acceptable_password('ashort') == False
#     assert is_acceptable_password('muchlonger5') == True
#     assert is_acceptable_password('sh5') == False
#     assert is_acceptable_password('1234567') == False
#     print("Coding complete? Click 'Check' to earn cool rewards!")


# def is_acceptable_password(password: str) -> bool:
        
#     numbers = "0,1,2,3,4,5,6,7,8,9".split(",")
#     letters = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z".split(",")
#     global output
#     output = False
#     number = False
#     letter = False
    
#     if len(password) < 9:
#         for i in numbers:
#             if i in password:
#                 number = True
#         for i in letters:
#             if i in password:
#                 letter = True
#         if letter == True and number == True:
#             if len(password) <= 6:
#                 output = False
#             else:
#                 output = True
#     else:
#         output = True
#     #print(f"Letter={letter}")
#     #print(f"number={number}")
#     #print(f"output={output}")
#     return(output)


# if __name__ == '__main__':
#     print("Example:")
#     print(is_acceptable_password('short'))

#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert is_acceptable_password('short') == False
#     assert is_acceptable_password('short54') == True
#     assert is_acceptable_password('muchlonger') == True
#     assert is_acceptable_password('ashort') == False
#     assert is_acceptable_password('muchlonger5') == True
#     assert is_acceptable_password('sh5') == False
#     assert is_acceptable_password('1234567') == False
#     assert is_acceptable_password('12345678910') == True
#     print("Coding complete? Click 'Check' to earn cool rewards!")
