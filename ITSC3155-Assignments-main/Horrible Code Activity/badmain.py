import random


class GameData:
    def __init__(self):
        self.games_played = 0
        self.player_wins = 0
        self.computer_wins = 0
        self.ties = 0

    def get_stats(self):
        print("Games Played: {}".format(self.games_played))
        print("Player Wins: {}".format(self.player_wins))
        print("Computer Wins: {}".format(self.computer_wins))
        print("Ties: {}".format(self.ties))

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "tie"

        # determines winner based on choices
        if user_choice == "rock":
            if computer_choice == "scissors":
                return "player"
            else:
                return "computer"
        elif user_choice == "paper":
            if computer_choice == "rock":
                return "player"
            else:
                return "computer"
        elif user_choice == "scissors":
            if computer_choice == "paper":
                return "player"
            else:
                return "computer"
        else:
            return "invalid"

def main():

    game_data = GameData()

    #rps game begins
    while True:
        user_choice = input("choose rock, paper, or scissors ('off' to quit): ").lower()

        if user_choice == 'off':
            print("thank you for playing!")
            break

        if user_choice not in ["rock", "paper", "scissors"]:
            print("invalid choice. please select only rock, paper, or scissors.")
            continue

        computer_choice = random.choice(["rock", "paper", "scissors"])
        print("computer chose: {}".format(computer_choice))

        # increments stats based on winner
        game_data.determine_winner(user_choice, computer_choice)
        game_data.games_played += 1

        game_data.get_stats()

if __name__ == "__main__":
    main()
