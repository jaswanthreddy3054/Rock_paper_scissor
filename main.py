import random

def game():
    while True:
        user_choice = input("Enter a choice (rock, paper, scissors): ").lower()
        while user_choice not in ["rock", "paper", "scissors"]:
            user_choice = input("Invalid input. Enter a choice (rock, paper, scissors): ").lower()

        possible_choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(possible_choices)
        print(f"\nUser chose {user_choice}, computer chose {computer_choice}.\n")

        if user_choice == computer_choice:
            print(f"Both chose {user_choice}. It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print(f"{user_choice.capitalize()} beats {computer_choice}! User wins!")
        else:
            print(f"{computer_choice.capitalize()} beats {user_choice}! Computer wins!")

        if input("Play again? (yes/no): ").lower() != "yes":
            break

if __name__ == "__main__":
    game()
