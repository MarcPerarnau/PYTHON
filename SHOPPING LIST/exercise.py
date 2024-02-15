cart = {}

next = True
while next:
    item = input('Enter a product: ')
    price = float(input("Entar a price of " + item + ": "))
    cart[item] = price
    next = input('Do you want to continue adding information (Yes/No): ').title() == "Yes"
cost = 0 
print('Shopping list')
for item, price in cart.items():
    print(item, '\t', price)
    cost += price
print('Total cost: ', round(cost,2), '$')
