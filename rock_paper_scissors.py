import random

def get_user_choice():
    while True:
        choice = input("Choose Rock, Paper, or Scissors: ").strip().lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        else:
            print("Invalid input. Please enter 'Rock', 'Paper', or 'Scissors'.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return 'tie'
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return 'user'
    else:
        return 'computer'

def display_result(user, computer, winner):
    print(f"\nYou chose: {user.capitalize()}")
    print(f"Computer chose: {computer.capitalize()}")
    if winner == 'tie':
        print("Result: It's a tie!")
    elif winner == 'user':
        print("Result: You win! 🎉")
    else:
        print("Result: You lose. 😢")

def play_game():
    user_score = 0
    computer_score = 0
    round_number = 1

    print("🎮 Welcome to Rock-Paper-Scissors!")
    print("Instructions: Enter Rock, Paper, or Scissors to play.\n")

    while True:
        print(f"\n--- Round {round_number} ---")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)

        display_result(user_choice, computer_choice, winner)

        if winner == 'user':
            user_score += 1
        elif winner == 'computer':
            computer_score += 1

        print(f"\nScore: You {user_score} - {computer_score} Computer")

        again = input("\nDo you want to play another round? (yes/no): ").strip().lower()
        if again not in ['yes', 'y']:
            print("\nThanks for playing! Final Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            break

        round_number += 1

if __name__ == "__main__":
    play_game()
