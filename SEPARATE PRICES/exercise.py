price = input("Enter a price with two decimals (xx.xx): ")

print(price[:price.find('.')], " euros and ",price[price.find('.')+1:] , "cents")
