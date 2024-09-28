import random
import gamedata
import choices


def main():
    # create instance of GameData
    game_data = gamedata.GameData()

    # while the game has started, user is prompted to choose between rps or quit
    while True:
        user_choice = input("choose between rock, paper, or scissors ('off' to quit): ").lower()
        if user_choice == "off":
            print("thank you for playing!")
            break

        # if user inputs anything other than rps_choices continue loop
        if user_choice not in choices.rps_choices:
            print("invalid choice. please select only rock, paper, or scissors.")
            continue

        # computer's choice is at random
        computer_choice = random.choice(list(choices.rps_choices))
        print("computer chose: {}".format(computer_choice))

        # determines the winner of the game
        winner = game_data.determine_winner(user_choice, computer_choice)

        # updates the stats based on the results of the game
        if winner == "tie":
            print("it's a tie!")
            game_data.increment_ties()
        elif winner == "player":
            print("congratulations, you win!")
            game_data.increment_player_wins()
        else:
            print("better luck next time, the computer wins!")
            game_data.increment_computer_wins()

        # when the game ends, increment the game's data
        game_data.increment_games_played()

        # print the game stats
        print(game_data.get_stats())


# call the main function to run the game
if __name__ == "__main__":
    main()
