

import random


LEXICON_FILE = "Lexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8             # Initial number of guesses player starts with


def play_game(secret_word):
    """
    1- We translate secret word to list 
    2- Assign array length to a value. (Dizi uzunluğunu bir değere ata)
    3- Creating a second empty list tire 

    6- 
    * With the "get_word" function, we choose a random word from the txt file.
    * In the main function, we give the secret_word as a value to the play_game function.
    * In the play_game function, we assign the initial_guess number to the "ig" variable. The "ig" variable will control the remaining right in the code.
    * We are adding the secret-word to the list. We assign this list length to the variable "i".
    With the *for loop, I put a hyphen as long as the word "secret_word" in a second list.

* We ask the user to make their first guess.
*Each prediction is checked for letters with the "control" function.
*If it is a letter, it is converted to uppercase in this function.

*
    """

    ig = INITIAL_GUESSES 
    list_1 =  list(secret_word)
    i = len(list_1)

    liste_2 = []
    for i in range (i-1):
        liste_2.append("-")
    print("The word now looks like this: ", listToString(liste_2))
    print("You have" ,ig," guesses left" )
    guess = (input("Type a single letter here, then press enter: "))
    guess =control (guess,ig)
    
    cont = 0
    ax =0
    while  ig > 0 :
            comp  =0
            for comp in range (i+1):
               
                if list_1[comp]  == guess:
                    liste_2 [comp]= guess
                    cont = 1
                    ax +=1

            if cont == 0 :
                    ig -= 1
                    cont = 0
                    print("There are no" , guess,"'s in the word")
                    
                    print("The word now looks like this: ",  listToString(liste_2))
                    
                    print("You have" ,ig," guesses left" )
                    if ig == 0:
                        print("Sorry, you lost. The secret word was:",  secret_word)
                        break

                    guess = (input("Type a single letter here, then press enter: "))
                    guess =control (guess,ig)
            else :
                print ("That guess is correct.")


                if ax == len(liste_2):
                        print("Congratulations, the word is: ", secret_word)
                        break

                else:
                    print("The word now looks like this: ", listToString(liste_2))
                    print("You have" ,ig," guesses left" )
                    guess =control (guess,ig)
                    guess = (input("Type a single letter here, then press enter: "))
                    guess =control (guess,ig)
            cont  =0
            


def control (guess, ig):


    for i in range (1000):
        if len(guess) == 1:
            
            if (ord(guess) >64 and ord(guess)< 91) or  (ord(guess) > 96 and ord(guess)< 123):
                
                return guess.upper()
                break
                
                    
            else:
                print("This is not correct form please try again.")
                guess = (input("Type a single letter here, then press enter: "))
        else:
            print ("Guess should only be a single character.")
            guess = input("Type a single letter here, then press enter: ")


def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    
    # return string  
    return str1 
def get_word():

    f = open(LEXICON_FILE)
    text = []
    i = 0
    for line in f:
	    text.append(line)
    long1 = len(text)
    
    index = random.randrange((long1-1))
    f.close()
    return text[index]

def main():

    secret_word = get_word()
    print("")
    print("~~~~~~~~~~ WELCOME ~~~~~~~~~~\n")
    
    play_game(secret_word)



if __name__ == "__main__":
    main()
