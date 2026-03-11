import random

def display_title():
    print("Guest the number!\n")

def main():
    display_title()
    again = "y"
    
    for i in range(0, 10):
        print(random.randint(1, 4))
if__name__ == "__main__":
    main()