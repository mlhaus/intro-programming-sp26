import random

def roll_die(turn, score, score_this_turn):
    die = random.randint(1, 6)
    print(f"Die: {die}")
    if(die == 1):
        score_this_turn = 0
        turn += 1
        print("Turn over. No score.\n")
        turn_over = True
    else:
        score_this_turn += die
        turn_over = False
    return turn, score, score_this_turn, turn_over

def hold_turn(turn, score, score_this_turn):
    print("Score for turn:", score_this_turn)
    score += score_this_turn
    print("Total score:", score, "\n")
    turn_over = True
    game_over = False
    if(score >= 20):
        turn_or_turns = "turn" if turn == 1 else "turns"
        print(f"You finished in {turn} {turn_or_turns}!")
        game_over = True
    turn += 1
    return turn, score, turn_over, game_over

def take_turn(turn, score, game_over):
    print("TURN", turn) # print the turn number
    score_this_turn = 0
    turn_over = False
    while(not turn_over):
        choice = input("Roll or hold? (r/h) ")
        if(choice.lower() == "roll" or choice.lower() == "r"):
            turn, score, score_this_turn, turn_over = roll_die(turn, score, score_this_turn)
        elif(choice.lower() == "hold" or choice.lower() == "h"):
            turn, score, turn_over, game_over = hold_turn(turn, score, score_this_turn)
        else:
            print("Invalid choice. Try again.")
    return turn, score, game_over
            
def display_rules():
    print("Let's PLAY PIG!")
    print()
    print("* See how many turns it takes you to get to 20.")
    print("* Turn ends when you hold or roll a 1.")
    print("* If you roll a 1, you lose all points for the turn.")
    print("* If you hold, you save all point for the turn.")

def play_game():
    turn = 1
    score = 0
    game_over = False
    while(not game_over):
        turn, score, game_over = take_turn(turn, score, game_over)
    print("\nGame over!")

def main():
    display_rules()
    play_game()

if __name__ == "__main__":
    main()