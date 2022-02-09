import random
import string

# def load_words():
#     '''
#     return: list of valid words; words ares trings of lowercase letters
#     '''
#     with open('/usr/share/dict/words') as infile:
#         word_list = infile.read().splitlines()
#     return word_list

# def choose_word(word_list):
#     return random.choice(word_list)
    

word_list = ['tiger', 'gamecock', 'baboon', 'camel', 'game', 'class', 'duck', 'water', 'soap', 'tissue']

chosen_word = random.choice(word_list)
guesses = ''
lives = 6
display = []
for letter in chosen_word:
    display += '_'

end_of_game = False

while end_of_game == False:
   
    guess = input('Guess a letter: ').lower()

    if guess in display:
        print(f"You've already guessed {guess}")



    for position in range(len(chosen_word)):
        letter= chosen_word[position]
        if letter == guess:
            display[position] = letter
    guesses += guess

    print(display)
    print(f'guesses {guesses}')
    

    if guess not in chosen_word:
        print(f"Your guess {guess} is wrong , you have {lives} remaining")
       
        lives -=1 
        if lives == 0:
            end_of_game = True
            print('You lose')
    if "_" not in display:
        end_of_game = True
        print('You Win')



# def is_word_guessed(secret_word, letters_guessed):
#     '''
#         secret_word: the word the user is guessing
#         letters_guessed: what letters have been guessed
#         return: boolean, True if all the letters of the secre_word are in letters_guessed, otherwise false
#     '''

#     for char in secret_word:
#         if not char in letters_guessed:
#             return True
        
#     return False


# def get_avaliable_letters(letters_guessed):
#     '''
#     letters_guesses: list, what letters have been guessed so far
#     return: string, comprised of letters that have not yet been guessed

#     '''

#     return ''.join([x for x in string.ascii_lowercase if x not in letters_guessed])
    

# def get_guessed_word(secret_word, letters_guessed):
#     '''
#     secret_word: string, the word the user is guessing
#     letters guessed:

#     return:string, comprised of letters and underscores that represents what letters in the secret word
#     '''
#     guessed_word = ''
#     for char in secret_word:
#         if char in letters_guessed:
#             guessed_word += char
#         else:
#             guessed_word += '_'

#         return guessed_word




# def hangman(secret_word):
#     '''
#     secretWord: string, the word to guess

#     Start a game of Hangman

#     *At the start of the game, let the user know how many letters the secret_word contains

#     *As the user to supply one guess (i.e. letter) per round

#     *The user should recieve feedback immediately after each guess about whether their guess appears in the randomly generated word

#     *After each round, you should display to the user the partially guessed word, as well as letters that the user has not yet guessed

#     '''

#     remaining_guesses = 8
#     letters_guessed = []

#     print("Welcome to hangman")
#     print('I am thinking of a word that is, str', str(len(secret_word)), 'letters long.')
#     while remaining_guesses > 0:
#         print('You have', remaining_guesses, 'guesses left')
#         print('Avaliable letters:', get_avaliable_letters(letters_guessed))
#         user_guess = input('Please guess a letter: ').lower

#         if user_guess in letters_guessed:
#             print("You already guessed that letter", get_guessed_word(secret_word, letters_guessed))
#         else:
#             letters_guessed.append(user_guess)

#             if user_guess in secret_word:
#                 print('good guess', get_guessed_word(
#                     secret_word, letters_guessed))
#             else:
#                 print('that letter  is not in the word',
#                     get_guessed_word(secret_word, letters_guessed))
#                 remaining_guesses -=1

#         if is_word_guessed(secret_word, letters_guessed):
#             print('You won!')
#             return
    
#     print('Sorry you ran out of guesses. The word was', secret_word)

    



