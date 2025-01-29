#Rock papar siscer
import random
choice_list = [0,1,2]

player_name = input("Enter your name \n")

choice_player = int(input("What do you choose?, Type 0 for Rock, 1 for paper or 2 for scissors \n"))

choice_system = random.choice(choice_list)

if choice_player >= 3 or choice_player < 0:
    print("you typed an invalid number you loose!")
elif choice_player == 0 and choice_system == 1:
    print(f"{player_name} loose")
elif choice_player == 1 and choice_system == 2:
    print(f"{player_name} loose")
elif choice_player == 2 and choice_system == 0:
    print(f"{player_name} won")
elif choice_player == 1 and choice_system == 0:
    print(f"{player_name} won")
elif choice_player == 2 and choice_system == 1:
    print(f"{player_name} won")
elif choice_player == 0 and choice_system == 2:
    print(f"{player_name} won")
elif choice_player == choice_system :
    print("It's a draw")


