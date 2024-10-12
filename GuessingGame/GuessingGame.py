# Name:stanley Ndika Ticha
# Course Number: Object
# Lab Title: Guessing Game
# 
import random 

def print_heading():
    print("Guess the number!")
    
def play_game(limit):
    random_number = random.randint(1,limit)
    guess_count = 0
    print(f"Guess the number between 1 and {limit}: ")
    while True:
        guess = int(input("Enter your guess: "))
        guess_count +=1
        if guess > random_number:
            print("Too high, try again")
        elif guess < random_number:
            print("Too low, try again")
        else:
            print(f"Congratulation! You have guessed the number! in {guess_count} time(s)")
            break
        
def main():
    print_heading()
    while True:
        limit = int(input("Enter the limit for the random number: "))
        play_game(limit)
        play_again = input("Would you like to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()