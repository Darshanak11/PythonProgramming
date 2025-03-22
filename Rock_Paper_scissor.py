import random

def get_user_choice():
    """Prompt the user until a valid choice is made."""
    while True:
        user_input = input("Enter your choice (rock, paper, scissors): ").strip().lower()
        if user_input in ['rock', 'paper', 'scissors']:
            return user_input
        print("Invalid input. Please try again.")

def get_computer_choice():
    """Randomly select a choice for the computer."""
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    """Determine the winner of the game based on classic rules."""
    if user == computer:
        return "It's a tie!"
    # Define winning scenarios: rock crushes scissors, scissors cuts paper, paper covers rock
    if ((user == 'rock' and computer == 'scissors') or
        (user == 'scissors' and computer == 'paper') or
        (user == 'paper' and computer == 'rock')):
        return "You win!"
    return "Computer wins!"

def play_game():
    """Main game loop."""
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        # Ask if the user wants to play again
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("Thanks for playing!")
            break
        print()  # Add a blank line for neatness between rounds

if __name__ == "__main__":
    play_game()
