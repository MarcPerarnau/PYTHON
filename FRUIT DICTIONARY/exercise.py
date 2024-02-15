frutas = {'Banana':1.35, 'Apple':0.8, 'Pear':0.85, 'Orange':0.7}
fruta = input('Wich fruit do you want? ').title()
kg = float(input('How many kg '))
if fruta in frutas:
    print(kg, 'ks of', fruta, 'worth', round(frutas[fruta]*kg,2), '$')
else: 
    print("The fruit is not here")
