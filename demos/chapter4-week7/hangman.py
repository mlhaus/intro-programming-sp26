# See flowchart mermaid code
# https://gemini.google.com/share/763e5d1b8a21

import random

def get_word():
    # List of words to choose from
    words = ['python', 'javascript', 'nodejs', 'React', 'angular', 'php', 'css', 'html']
    return random.choice(words).lower()

def display_hangman(tries):
    stages = [  # Final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                """,
                # Head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                """,
                # Head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                """,
                # Head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                """,
                # Head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                """,
                # Head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                """,
                # Initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                """
    ]
    return stages[tries]

def play():
    word = get_word()
    word_letters = set(word) #removes duplicate letters
    guessed_letters = set()
    tries = 6

    print("Let's play Hangman!")
    
    while len(word_letters) > 0 and tries > 0:
        print(display_hangman(tries))
        print(f"Guessed letters: {' '.join(guessed_letters)}")
        word_display = [letter if letter in guessed_letters else '_' for letter in word]
        print(f"Current word: {' '.join(word_display)}")

        guess = input("Guess a letter: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You've already guessed that letter.")
            elif guess in word_letters:
                word_letters.remove(guess)
                guessed_letters.add(guess)
                print(f"Good job! {guess} is in the word.")
            else:
                tries -= 1
                guessed_letters.add(guess)
                print(f"Sorry, {guess} is not in the word.")
        else:
            print("Invalid input. Please enter a single letter.")

    if tries == 0:
        print(display_hangman(0))
        print(f"You lost! The word was {word}.")
    else:
        print(f"Congratulations! You guessed the word {word}.")

if __name__ == "__main__":
    play()