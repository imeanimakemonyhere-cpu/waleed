#Gussing game:
#This code made me feel like i am getting better.......................

import random

def get_difficulty():
    """Let the user choose a difficulty level."""
    while True:
        print("\nSelect a Difficulty Level: ")
        print("1. Easy (1, 50)")
        print("2. Medium (1, 100)")
        print("3. Hard (1, 300)")
        choice = input("Enter Choice (1-3): ")
        if choice == "1":
            return 1, 50
        elif choice == "2":
            return 1, 100
        elif choice == "3":
            return 1, 300
        else:
            print("Invalid Choice. Try (1-3) Method.")

def play_game(lowest, highest):
    """Main game logic."""
    answer = random.randint(lowest, highest)
    guesses = 0
    is_running = True

    print(f"\nGuess a number between {lowest} and {highest}.")
    while is_running:
         
         try:
            guess = int(input("Enter Your Guess: "))
            if guess <  lowest or guess > highest:
                print(f"Please guess a number within {lowest} or {highest}.")
            elif guess < answer:
                print(f"Too Low! Try again. (guesses:{guesses + 1})")
                guesses += 1
            elif guess > answer:
                print(f"Too high! Try again. (guesses:{guesses + 1})")
                guesses += 1
            else:
                guesses += 1
                print(f"\nCorrect! You guessed {answer} in {guesses} Attempts.")
                is_running = False
         except ValueError:
            print("Ivalid input. Please enter a valid numbers.")

def main():
    """Main function"""
    print("Welcome Guessing Game!.")

    while True:
        lowest, highest = get_difficulty()
        play_game(lowest, highest)

        replay = input("\nPlay again? (yes/no):").lower()
        if replay != 'yes':
            print("Thanks for playing! Goodbye.")
            break
        
        
if __name__ == "__main__":
    main()



