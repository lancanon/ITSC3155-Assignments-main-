# keeps track of game record

class GameData:

    # set initial counts for the game's statistics
    def __init__(self):
        self.games_played = 0
        self.player_wins = 0
        self.computer_wins = 0
        self.ties = 0

    # increment the total number of games played
    def increment_games_played(self):
        self.games_played += 1

    # increments the player's win count
    def increment_player_wins(self):
        self.player_wins += 1

    # increments the computer's win count
    def increment_computer_wins(self):
        self.computer_wins += 1

    #increments the tie count for drawed games
    def increment_ties(self):
        self.ties += 1

    # determines the winner of the game
    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "tie"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
                (user_choice == "paper" and computer_choice == "rock") or \
                (user_choice == "scissors" and computer_choice == "paper"):
            return "player"
        else:
            return "computer"

    # get a summary of the game's statistics
    def get_stats(self):
        return (
            "Games Played: {}\n"
            "Player Wins: {}\n"
            "Computer Wins: {}\n"
            "Ties: {}".format(self.games_played, self.player_wins, self.computer_wins, self.ties)
        )
