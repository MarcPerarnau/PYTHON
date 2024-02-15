person = {}

next = True
while next:
    data = input('What data do you want to enter: ')
    value = input(data + ': ')
    person[data] = value
    print(person)
    next = input('Do you want to continue adding information (Yes/No): ').title() == "Yes"
