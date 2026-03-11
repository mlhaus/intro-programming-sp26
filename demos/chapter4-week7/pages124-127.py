import random

LIMIT = 2

def display_title():
    print("Guess the number!\n")

def play_game():
    rand_number = random.randint(1, LIMIT)
    print(f"I am thinking of a number from 1 to {LIMIT}")
    count = 1
    while(guess := int(input("Your guess: "))) != rand_number:
        if(guess < rand_number):
            print("Too low.")
        elif(guess > rand_number):
            print("Too high")
        count += 1
    try_or_tries = "try" if count == 1 else "tries"
    print(f"You guessed it in {count} {try_or_tries}.\n")

def main():
    display_title()
    again = "y"
    while(again.lower() == "y"):
        play_game()
        again = input("Would you like to play again? (y/n): ")
        print()
    print("Bye!")

if __name__ == "__main__":
    main()