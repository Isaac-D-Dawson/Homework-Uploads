# Your task is to decrypt the secret message using the Morse code.
# The message will consist of words with 3 spaces between them and 1 space between each letter of each word.
# If the decrypted text starts with a letter then you'll have to print this letter in uppercase.

# example

# Input: The secret message.

# Output: The decrypted text.

# Precondition:
# 0 < len(message) < 100
# The message will consists of numbers and English letters only.

MORSE = {'.-':    'a', '-...':  'b', '-.-.':  'c',
         '-..':   'd', '.':     'e', '..-.':  'f',
         '--.':   'g', '....':  'h', '..':    'i',
         '.---':  'j', '-.-':   'k', '.-..':  'l',
         '--':    'm', '-.':    'n', '---':   'o',
         '.--.':  'p', '--.-':  'q', '.-.':   'r',
         '...':   's', '-':     't', '..-':   'u',
         '...-':  'v', '.--':   'w', '-..-':  'x',
         '-.--':  'y', '--..':  'z', '-----': '0',
         '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9'
        }

def morse_decoder(code):
    
    inval = code.split("   ")#get it as individual words)
    
    #We do the first word maually to ensure valid capitaliseation
    currentWord = inval[0].split(" ")
    
    outval = MORSE[currentWord[0]].upper()
    
    for i in currentWord[1:]:
        outval = f"{outval}{MORSE[i]}"
    
    #Now we decode the rest normally
    
    for i in inval[1:]:
        outval = f"{outval} "
        for j in i.split(" "):
            outval = f"{outval}{MORSE[j]}"
    

    print(outval)#Debug call
    return(outval)
    
# if __name__ == '__main__':
#     print("Example:")
#     print(morse_decoder('... --- ...'))

#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert morse_decoder("... --- -- .   - . -..- -") == "Some text"
#     assert morse_decoder("..--- ----- .---- ---..") == "2018"
#     assert morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--") == "It was a good day"
#     print("Coding complete? Click 'Check' to earn cool rewards!")
