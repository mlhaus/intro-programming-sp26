def calculateFutureValue(monthlyInvestment, monthlyRate, months):
    futureValue = 0
    for i in range(months):
        futureValue = (futureValue + monthlyInvestment) * (1 + monthlyRate)
    return futureValue

futureValue = calculateFutureValue(500, 0.04/12, 120)
print(futureValue)