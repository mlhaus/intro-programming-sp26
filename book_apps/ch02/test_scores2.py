'''
FILE:           test_scores2.py
DATE:           2026-01-21
AUTHOR:         Marc Hauschildt
DESCRIPTION:    This is a tutorial program that illustrates the use of 
                the while and if statements
'''

'''
declare variables
to track the count, total score
and average score
'''
counter = 0
score_total = 0
test_score = 0

# Prompt user for test scores
while test_score != 999:
    test_score = int(input("Enter test score (or 999 to quit): "))
    if test_score >= 0 and test_score <= 100:
        score_total += test_score  # add score to total
        counter += 1  # add 1 to counter

# calculate average score
average_score = score_total / counter
average_score = round(average_score)

# print results
print("Total score: " + str(score_total) + "\nAverage \
score: " + str(average_score))