score = int(input("Enter test score: "))

if score >= 90 and score <= 100: 
    grade = "A"
elif score >= 80 and score < 90: 
    grade = "B"
elif score >= 70 and score < 80: 
    grade = "C"
elif score >= 60 and score < 70: 
    grade = "D"
elif score >= 0 and score < 60: 
    grade = "F"
else: 
    grade = "Invalid"
    
print(f"Score: {score}\nGrade: {grade}")


# score = int(input("Enter test score: "))

# if score < 60: 
#     grade = "F"
# elif score < 70: 
#     grade = "D"
# elif score < 80: 
#     grade = "C"
# elif score < 90: 
#     grade = "B"
# else: 
#     grade = "A"
    
# print(f"Score: {score}\nGrade: {grade}")

# score = int(input("Enter test score: "))

# if score >= 90: 
#     grade = "A"
# elif score >= 80: 
#     grade = "B"
# elif score >= 70: 
#     grade = "C"
# elif score >= 60: 
#     grade = "D"
# else: 
#     grade = "F"
    
# print(f"Score: {score}\nGrade: {grade}")