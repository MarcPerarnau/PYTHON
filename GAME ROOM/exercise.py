year = float(input("Enter your age: "))

if year < 4:
    price = 0
elif year < 18:
    price = 5
elif year > 18:
    price = 10

print("You have to pay ", price, "$")
