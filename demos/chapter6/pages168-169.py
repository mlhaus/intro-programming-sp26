numbers = [8, 1, 9, 2, 6, 7]
sum = 0
sum_evens = 0
sum_odds = 0
evens = []
odds = []
for number in numbers:
    sum += number
    if(number % 2 == 0):
        sum_evens += number
        evens.append(number)
    else:
        sum_odds += number
        odds.append(number)
print(*numbers, sep=" + ", end=" ")
print(f"= {sum}")
print(f"Average is {sum / len(numbers)}")
print(f"Highest is {max(numbers)}")
print(f"Lowest is {min(numbers)}")

print(*evens, sep=" + ", end=" ")
print(f"= {sum_evens}")
print(f"Average is {sum_evens / len(evens)}")

print(*odds, sep=" + ", end=" ")
print(f"= {sum_odds}")
print(f"Average is {sum_odds / len(odds)}")