class GameView():
    def show_current_word(self, player_word):
        print(player_word)

    def intro(self):
        print('\nWelcome to a really boring version of Wordle!')
        print('---------------------------------------------')
    
    def get_word_guess(self):
        return input('What is your guess? (5 letters) ').lower()

    def display_turns_left(self, turns):
        print(f'You have {turns} turns left.')

    def display_letters_guessed(self, letters_guessed):
        print(f'Letters guessed: {letters_guessed}')

    def display_no_turns(self, choice):
        print('No more turns. You lose.')
        print(f'The word is {choice}.')
    
    def display_target_reached(self):
        print('You got the word!!')
    

