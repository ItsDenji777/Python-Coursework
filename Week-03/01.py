user_grade = input("What grade did you get? ")

user_grade = user_grade.upper()

if user_grade == "A":
    print("Good Job! You got a grade between 17-20")
elif user_grade == "B":
    print("You got a grade between 14-17")
elif user_grade == "C":
    print("You got a grade between 10-14")
elif user_grade == "F":
    print("You failed! Your grade is between 0-10")
else:
    print(f"'{user_grade}' is not defined as a Grade!")