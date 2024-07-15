import random
import time

def play_game():
    number = random.randint(1, 100)
    attempts = 0
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
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number} in {attempts} attempts.")
            break

def main_menu():
    while True:
        print("Welcome to the Guess the Number game!")
        print("1. Play Game")
        print("2. Quit")
        choice = input("Enter your choice: ")
        if choice == '1':
            play_game()
        elif choice == '2':
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Invalid choice! Please enter 1 or 2.")

main_menu()
time.sleep(1)
print("Exiting game...")
