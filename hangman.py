import string
from words import choose_word
from images import IMAGES

'''
Important instruction
* function and variable name snake_case -> is_prime
* contant variable upper case PI
'''


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns: 
      return True (if user guess the world correctly )
      return False (wrong selection)
    '''
    s =secret_word
    for i in letters_guessed:
        s=s.replace(i,"")

    if s =="":
        return True

    return False


# if you want to test this function please call function -> get_guessed_word("kindness", [k, n, d])


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns: 
      return string which contain all the right guessed characters
      Example :- 
      if secret_word -> "kindness" and letters_guessed = [k, n, s]
      return "k_n_n_ss"
    '''
    index = 0
    guessed_word = ""
    while index < len(secret_word):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list contains all guessed characters
    returns: 
      it return string which contains all characters except guessed letters
    Example :-
      letters_guessed = ['e', 'a'] then    
      return sting is -> `bcdfghijklmnopqrstuvwxyz`
    '''
    letters_left = string.ascii_lowercase
    for l in letters_guessed:
        letters_left = letters_left.replace(l, "")

    return letters_left


def isvalid(letter, available_letters):
    if letter == "hint":
        return True
    elif letter in available_letters and len(letter) == 1:
        return True
    return False


def hangman(secret_word):
    '''
    secret_word (string) : secret word to guessed by the user.

    Steps to start Hangman:

    * In the beginning of the game user will know about the total characters in the secret_word    

    * In each round user will guess one character 

    * After each character give feedback to the user
      * right or wrong

    * Display partial word guessed by the user and use underscore in place of not guess word    
    '''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {} letters long.".format(
        str(len(secret_word))), end='\n\n')

    letters_guessed = []
    TOTAL_LIVES = 0
    is_hint_used = False
    while TOTAL_LIVES < 8:
        available_letters = get_available_letters(letters_guessed)
        print("Available letters: {} ".format(available_letters))

        guess = input("Please guess a letter: ")
        letter = guess.lower()
        if letter == "hint":
            if is_hint_used:
                print("Sorry u have already used the hint !")
            is_hint_used = True
            is_used_alread = True
            for i in secret_word:
                if i not in letters_guessed:
                    letters_guessed.append(i)
                    print("hint :", i)
                    break
                print("Good guess: {} ".format(
                    get_guessed_word(secret_word, letters_guessed)))
                if is_word_guessed(secret_word, letters_guessed):
                    print(" * * Congratulations, you won! * * ", end='\n\n')
                    break

        if not isvalid(letter, available_letters):
            print("please enter a valid letter !")
            continue

        if letter in secret_word:
            letters_guessed.append(letter)
            print("Good guess: {} ".format(
                get_guessed_word(secret_word, letters_guessed)))
            if is_word_guessed(secret_word, letters_guessed):
                print(" * * Congratulations, you won! * * ", end='\n\n')
                break
        else:
            if is_used_alread:
                continue
            print("Oops! That letter is not in my word: {} ".format(
                get_guessed_word(secret_word, letters_guessed)))
            letters_guessed.append(letter)
            print("")
            print("you have ", 8 - TOTAL_LIVES - 1, " more lives !")
            TOTAL_LIVES += 1
            print(IMAGES[TOTAL_LIVES])


# Load the list of words into the variable wordlist
# So that it can be accessed from anywhere in the program
secret_word = choose_word()
print(secret_word)
hangman(secret_word)
