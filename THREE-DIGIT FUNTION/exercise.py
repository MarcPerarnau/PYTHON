def number_max(number1, number2, number3):
    return max(number1, number2, number3)

number1 = int(input("Enter a first number: "))
number2 = int(input("Enter a second number: "))
number3 = int(input("Enter a third number: "))

result = number_max(number1, number2, number3)

print("The highest number is:", result)
