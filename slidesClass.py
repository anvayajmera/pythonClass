import random
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def play_game(difficulty):
    number = random.randint(1, 100)
    attempts = 0
    score = 1000
    while True:
        guess = input("Guess a number between 1 and 100: ")
        try:
            guess = int(guess)
            if guess < 1 or guess > 100:
                print("Out of bounds! Please try again.")
                continue
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        attempts += 1
        score -= 10 * difficulty
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number} in {attempts} attempts. Your score: {score}")
            return score

def main_menu():
    while True:
        clear_screen()
        print("Welcome to the Advanced Guess the Number Game!")
        print("1. Play Easy")
        print("2. Play Medium")
        print("3. Play Hard")
        print("4. View Leaderboard")
        print("5. Quit")
        choice = input("Enter your choice: ")
        if choice in ['1', '2', '3']:
            difficulty = int(choice)
            score = play_game(difficulty)
            update_leaderboard(score)
        elif choice == '4':
            view_leaderboard()
        elif choice == '5':
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Invalid choice! Please enter a number from 1 to 5.")
            time.sleep(1)

def update_leaderboard(score):
    name = input("Enter your name: ")
    with open("leaderboard.txt", "a") as f:
        f.write(f"{name} {score}\n")

def view_leaderboard():
    clear_screen()
    print("Leaderboard:")
    try:
        with open("leaderboard.txt", "r") as f:
            scores = [line.strip().split() for line in f]
            scores.sort(key=lambda x: int(x[1]), reverse=True)
            for i, (name, score) in enumerate(scores[:10], 1):
                print(f"{i}. {name} - {score}")
    except FileNotFoundError:
        print("No scores yet. Play the game to add your score!")
    input("Press Enter to return to the main menu.")

main_menu()
time.sleep(1)
print("Exiting game...")
