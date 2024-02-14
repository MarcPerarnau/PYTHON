income = float(input("Enter a annual income: "))

if income < 10000:
    emblem = 5
elif income < 20000:
    emblem = 15
elif income < 35000:
    emblem = 20
elif income < 60000:
    emblem = 30
elif income > 60000:
    emblem = 40

print("You have to pay ", income * emblem / 100, "$")
