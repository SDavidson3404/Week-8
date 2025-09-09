def gradeCalc(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Asks user for five inputs
score = int(input("Please enter your first score: "))
score2 = int(input("Please enter your second score: "))
score3 = int(input("Please enter your third score: "))
score4 = int(input("Please enter your fourth score: "))
score5 = int(input("Please enter your fifth score: "))
# Stores scores in list
scoreList = [score, score2, score3, score4, score5]
# Calculates Average
average = (score + score2 + score3 + score4 + score5) / 5
# Calculates Grades for scores
grade = gradeCalc(score)
grade2 = gradeCalc(score2)
grade3 = gradeCalc(score3)
grade4 = gradeCalc(score4)
grade5 = gradeCalc(score5)
avGrade = gradeCalc(average)
# Displays Scores, Average, and Grades
print(f"""Score 1: {score}
Grade 1: {grade}
Score 2: {score2}
Grade 2: {grade2}
Score 3: {score3}
Grade 3: {grade3}
Score 4: {score4}
Grade 4: {grade4}
Score 5: {score5}
Grade 5: {grade5}
Average: {average}
Average Grade: {avGrade}""")
# Saves Scores, Average, and Grades to file.
with open("Grades.txt", "w") as file:
    file.write(f"""Score 1: {score}
Grade 1: {grade}
Score 2: {score2}
Grade 2: {grade2}
Score 3: {score3}
Grade 3: {grade3}
Score 4: {score4}
Grade 4: {grade4}
Score 5: {score5}
Grade 5: {grade5}
Average: {average}
Average Grade: {avGrade}""")