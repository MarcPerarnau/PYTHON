subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
scores = []
for subject in subjects:
    score = input("What grade did you get in " + subject + "?")
    scores.append(score)
for i in range(len(subjects)):
    print("In " + subjects[i] + " you have " + scores[i])
