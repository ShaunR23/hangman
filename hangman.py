import random

word_list = ['tiger', 'gamecock', 'baboon', 'camel', 'game', 'class', 'duck', 'water', 'soap', 'tissue']

chosen_word = random.choice(word_list)
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

    print(display)
    

    if guess not in chosen_word:
        print(f"Your guess {guess} is wrong , you have {lives} remaining")
        lives -=1 
        if lives == 0:
            end_of_game = True
            print('You lose')
    if "_" not in display:
        end_of_game = True
        print('You Win')
    



