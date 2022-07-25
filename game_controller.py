from model.game import Game
from view.game_view import GameView

class GameController:
    def __init__(self, model: Game, view: GameView) -> None:
        self.model = model
        self.view = view
    
    def run_game(self):
        self.view.intro()
        choice = self.model.choose_word()
        while not self.model.is_terminated_turns():
            guess = self.view.get_word_guess()
            if self.model.is_terminated_win(choice, guess):
                self.view.display_target_reached()
                break
            player_word = self.model.check_user_guess(guess, choice)
            self.view.show_current_word(player_word)
            turns = self.model.turns_left()
            letters_guessed = self.model.letters_guess(guess, choice)
            self.view.display_letters_guessed(letters_guessed)
            self.view.display_turns_left(turns)
        
        if self.model.is_terminated_turns():
            self.view.display_no_turns(choice)
        
            
        
                

            
    

