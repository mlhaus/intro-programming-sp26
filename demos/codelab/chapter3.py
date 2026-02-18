# 51944
val1 = input()
n = 0
while(val1 != "xxxxx"):
	val2 = input()
	if(val1 != val2):
		n += 1
		val1 = val2
	else:
		while(val1 == val2):
			val1 = input()
			
# 51269
is_prime = False
if(n >= 2):
	is_prime = True
	for i in range (2, n):
		if(n % i == 0):
			is_prime = False
			break

# 51931
for i in range(5, 175, 5):
	print(i)

# 51187
i = lo
while(i <= hi):
	result += i
	i += 1

# 51253
start = k # 10
end = m # 40
count = 0
while(start <= end):
	if((start ** 0.5).is_integer()):
		count += 1
	start += 1
q = count

# 51165
number_of_prizes % number_of_participants == 0

# 51120
if(temperature > 98.6):
	fever = True
else:
	fever = False

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