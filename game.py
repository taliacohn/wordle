from ntpath import join
import random
from model.read_file import ReadFile

class Game:
    def __init__(self, file_path, word_length=5) -> None:
        self.word_length = word_length
        self.player_word = ['-' for i in range(word_length)]
        self.turns = 6 
        self.file_path = file_path
        self.letters_guessed = []

    # def choose_word(self):
    #     try:
    #         with open(self.file_path) as f:
    #             line = f.readline()
    #             while line:
    #                 fields = line.split()
    #                 choice = random.choice(fields)
    #                 line = f.readline()
    #         return choice
    #     except FileNotFoundError:
    #         print('file not found')

    def choose_word(self):
        x = ReadFile(self.file_path)
        self.fields = x.read_file()
        choice = random.choice(self.fields)
        return choice
    
    def check_user_guess(self, guess, choice):
        if len(guess) == 5:
            for i, letter in enumerate(guess):
                if choice[i] == guess[i]:
                    self.player_word[i] = '*'
                elif letter in choice and not choice[:i]:
                    self.player_word[i] = '+'
                else:
                    self.player_word[i] = '-'
            return ''.join(self.player_word)
            #return self.player_word
    
    def letters_guess(self, guess, choice):
        for i, letter in enumerate(guess):
            if letter not in choice:
                if letter not in self.letters_guessed:
                    self.letters_guessed += letter
        
        new_letters_guessed = ''.join(self.letters_guessed)
        return new_letters_guessed

    def turns_left(self):
        self.turns -= 1
        return self.turns

    #check if game is over
    def is_terminated_turns(self):
        return self.turns == 0

    def is_terminated_win(self, choice, guess):
        return choice == guess

    
       


                


    
    
    
