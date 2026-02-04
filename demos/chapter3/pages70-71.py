game_over = False # flag variable (should I continue, or should I stop)
while(not game_over):
    prompt = "Would you like to quit? [Yes or No]"
    print(prompt, end=" ")
    answer = input()
    if(answer.upper() == "YES" or answer.lower() == "y"):
        game_over = True

print("Good bye!")