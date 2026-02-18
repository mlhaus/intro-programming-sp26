for i in range(1, 10):
    for j in range(1, 10):
        print(f"{(i * j):2}", end=" ")
    print()
print()

# Get three valid test scores (0-100)
# Use a for loop when you know the loop should run an exact number of times
total_score = 0
for i in range(3):
    # Use a while loop when you are unsure of the number of times 
    # you need to prompt the user for valid input
    while True:
        print("Enter a test score (0-100): ", end="")
        score = float(input())
        if(score >= 0 and score <= 100):
            total_score += score
            break # end the while loop
        else: 
            print("Invalid test score")
print(f"Total score is {total_score}")