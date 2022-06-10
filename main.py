import random

comp_wins = 0
player_wins = 0

def choose_option() :
    user_choice = input("Choose R, P or S: ")
    if user_choice in ["Rock", "ROCK", "rock", "R", "r"]:
        user_choice = "r"

    elif user_choice in ["Paper", "PAPER", "paper", "P", "p"]:
        user_choice = "p"

    elif user_choice in ["Scissors", "SCISSORS", "scissors", "S", "s"]:
        user_choice = "s"

    else:
        print("Invalid option. Choose again.")
        choose_option()
    return user_choice

def Computer_Option():
    comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice = "r"

    elif comp_choice == 2:
        comp_choice = "p"

    else:
        comp_choice = "s"
        return comp_choice

while True:
    print("")
    user_choice = choose_option()
    comp_choice = Computer_Option()
    print("")

    if user_choice == "r":
        if comp_choice == "r":
            print("Player(Rock) : CPU(Rock). You tied.")
        elif comp_choice == "p":
            print("Player(Rock) : CPU(Paper). You lose!")
            comp_wins += 1
        elif comp_choice == "s":
            print("Player(Rock) : CPU(Scissors). You Win!")
            player_wins += 1

    elif user_choice == "p":
        if comp_choice == "r":
            print("Player(Paper) : CPU(Rock). You win!")
            player_wins += 1
        elif comp_choice == "p":
            print("Player(Paper) : CPU(Paper). You tied.")
        elif comp_choice == "s":
            print("Player(Paper) : CPU(Scissors). You lose!")
            comp_wins += 1

    elif user_choice == "s":
        if comp_choice == "r":
            print("Player(Scissors) : CPU(Rock). You lose!")
            comp_wins += 1
        elif comp_choice == "p":
            print("Player(Scissors) : CPU(Paper). You Win!")
            player_wins += 1
        elif comp_choice == "s":
            print("Player(Scissors) : CPU(Scissors). You tied.")
            
    print("")
    print("Player wins: " + str(player_wins))
    print("Computer wins: " + str(comp_wins))
    print("")

    user_choice = input("Do you want to play again? (y/n): ")
    if user_choice in ["Y", "y", "Yes", "yes", "YES"] :
        pass
    elif user_choice in ["N", "n", "No", "no", "NO"] :
        break
    else:
        break
            
