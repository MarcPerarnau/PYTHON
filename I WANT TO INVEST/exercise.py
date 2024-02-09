amount = float(input("Amount to invest?: "))
interest = float(input("Annual percentage interest?: "))
years = int(input("Years?: "))

print("Final capital: "+ str(round(amount * (interest / 100 + 1)** years, 2)))
