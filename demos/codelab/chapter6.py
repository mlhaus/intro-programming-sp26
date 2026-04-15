# 51702
len(t)

#51700
t = () # parenthesis define a tuple, brackets define a list

#51194
denominations = [1, 5, 10, 25, 50, 100]

# 51193
plist = []
for i in range(10, 101, 10): # start at 10, stop before 101, increase by 10 each time
    plist.append(i)

# 51204
plist[k] = 15

#51197
x = plist[-2]

#51616
play_list[0:3] = "spam","eggs","vikings"

#51615
play_list[k : j]

#51275
list3 = []
for i in range(len(list1)):
	list3.append(list1[i])
	list3.append(list2[i])

#51607
alist.pop(0)

#51295
new_list = []
for el in lst1:
	if(el in lst2):
		new_list.append(el)
new_list.sort()

#51256
words.reverse()

#51213
is_a_member = member_id in current_members

#51621
k in play_list

#51219
if(len(parking_tickets) == 0):
	most_tickets = 0
else:
	most_tickets = max(parking_tickets)


# 51283
largestIndex = 0
for i in range(1, len(names)):
	if(names[i] > names[largestIndex]):
		largestIndex = i
namePopped = names.pop(largestIndex)
names.insert(largestIndex, names.pop())
names.append(namePopped)	

# 51210
total = 0
total = sum(temps)
#for k in range(len(temps)):
#	total += temps[k]
#for temp in temps: 
#	total += temp
avg_temp = total / len(temps)

# 51215
j = len(zipcode_list)
k = len(set(zipcode_list))
duplicates = j != k

#duplicates = False
#for k in range(len(zipcode_list) - 1):
#	for j in range(k + 1, len(zipcode_list)):
#		if(zipcode_list[j] == zipcode_list[k]):
#			duplicates = True
#			break

