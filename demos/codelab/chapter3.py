# 51897
if(isIsosceles):
	isoCount += 1
	triangleCount += 1
	polygonCount += 1

# 51898
if(speed < 0):
	reverseDrivers += 1
elif(speed < 1):
	parkedDrivers += 1
elif(speed < 40):
	slowDrivers += 1
elif(speed <= 65):
	safeDrivers += 1
else:
	speeders += 1

# 51122
if(pH < 7):
	neutral = 0
	base = 0
	acid = 1
elif(pH > 7):
	neutral = 0
	base = 1
	acid = 0
else:
	neutral = 1
	base = 0
	acid = 0


#51896
if(gpa > 3.5):
	deansList += 1
	print(studentName)

#51884
c == "\t"

#51064
#this is an expression (the part that would appear after a variable assignment = operator)
not is_empty and number_of_credits > 2 
# this is a statement (assigning an expression to a variable, or printing the variable)
result = not is_empty and number_of_credits > 2 
print(result) 