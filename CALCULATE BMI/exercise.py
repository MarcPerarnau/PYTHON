Weight = input("Enter your weight in kg: ")
Height = input("Enter your height in mts: ")

bmi = round(float(Weight)/float(Height)**2,2)

print("Your body mass index is: ", bmi)
