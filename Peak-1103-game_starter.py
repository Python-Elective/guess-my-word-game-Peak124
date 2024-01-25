#help by Tarit and CHATGPT


# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "word_list.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Reading word_list file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # word_list: list of strings
    word_list = line.split()
    print(len(word_list), "words found")
    return word_list

def choose_word(word_list):
    """
    word_list (list): list of words (strings)

    Returns a word from word_list at random
    """
    return random.choice(word_list)

# end of helper code
# -----------------------------------

# Load the list of words into the variable word_list
# so that it can be accessed from anywhere in the program
word_list = load_words()

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...

    for letter in secret_word:
      if letter not in letters_guessed:
        return False
      
    return True

    #pseudocode
    # for every letter in secret_word:
    #     check if letter is in letters_guessed
    #       stop looking and return false

    #All letters guessed correctly, so return True




# ### Testcases
# print(is_word_guessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's']))
# print(is_word_guessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']))
# print(is_word_guessed('pineapple', []))



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
      #pseudocode
      #output string
        #for every letter in secret_word
        # check if letter in secret word
        #   concatenate += letter onto output_string
        # otherwise
        #   concatenate += underscore space '__' onto our
        #return output_string
    
    output_string = ''
        
    for letter in secret_word:
        if letter in letters_guessed:
            output_string += letter
        else:
           output_string += '_'

    return output_string
    pass
    
    
    
# Testcases
# print(get_guessed_word('apple', ['e', 'i', 'k', 'p', 'r', 's']))
# print(get_guessed_word('durian', ['a', 'c', 'd', 'h', 'i', 'm', 'n', 'r', 't', 'u']))

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...

    import string

    #option 1
    # for letter in letters_guessed:
    #   alphabet = alphabet.replace(letter,'')

    #option 2
    # alphabet = string.ascii_lowercase 

    # for letter in alphabet:
    #     if letter in letters_guessed:
    #       alphabet.remove(letter)
      
    # return ''.join(alphabet)


    #option 3
    #output_string = ''
    # for every letter in alphabet
    #   if letter in not letter_guessed:
    #     letter is still available
    #     concatenate letter onto output_string
    #   otherwise
    #     do nothing
    # return output string

    alphabet = string.ascii_lowercase

    output_string = ''
    for letter in alphabet:
        if letter not in letters_guessed:
            output_string += letter

    return output_string
          
    #pass
      
    
#Testcases 
# print(get_available_letters(['e', 'i', 'k', 'p', 'r', 's']) )
# print(get_available_letters([]))
  
def game_loop(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game.

    * At the start of the game, let the user know how many 
      letters the secret_word contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    letters_guessed = []
    mistakes_made = 0
    max_attempts = 8
    attempts = max_attempts

    print()
    print('Let the game begin!!!')
    print('I am thinking of a word with', len(secret_word), 'letters')
    
    while attempts > 0:
      print("You have", attempts, "attempts left")
      print(f"Letters available: {get_available_letters(letters_guessed)}")
      guess = input("Guess a letter!: ")

      if guess in letters_guessed:
        print("You tried this letter already!!:")
        print(get_guessed_word(secret_word, letters_guessed))
      elif guess in secret_word:
        letters_guessed.append(guess)
        print(f"Correct!!, available letters: {get_available_letters(letters_guessed)}")
        print(get_guessed_word(secret_word, letters_guessed))
      else:
        print(f"Incorrect, this letter isn't in my word!: {get_guessed_word(secret_word, letters_guessed)}")
        letters_guessed.append(guess)
        attempts -= 1

      print()

      if all(letter in letters_guessed for letter in secret_word):
        print('----------')
        print('You win!!, the word was', secret_word)
        print('It took you:', max_attempts - attempts, 'tries')
        break

      if attempts == 0:
        print('----------')
        print('You lose!!, the word was', secret_word)
        print()
        break
        

      
    
    # while True:   #game true
    #     if player == dead
    #       you dieee
    #       break

    #     if points == 0
    #       you loooooose
    #       break

    #     if guess_word == True
    #       you WIN
    #       break



def main():
    secret_word = choose_word(word_list)
    game_loop('gamers')    #secret word


# Testcases
# you might want to pick your own
# secret_word while you're testing


if __name__ == "__main__":
    main()