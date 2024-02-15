course = {'Mathematics':6, 'Physics':4, 'Chemistry':5}
total_credits = 0
for subjects, credits in course.items():
    print(subjects, 'have', credits, 'credits')
    total_credits += credits
print('The total number of the credits in the course is: ', total_credits)
