# Create a program that gets the average grade of 3 tests
# display students grade and letter grade 
# and tell student if she/he has passed  or failed the class

grade1 = int(input("Enter a grade 1 : ")) 
grade2 = int(input("Enter a grade 2 : ")) 
grade3 = int(input("Enter a grade 3 : "))
average = (grade1 + grade2 + grade3) / 3
letterGrade = ""
passed = False
if average >= 90:
  letterGrade = 'A'
  passed = True
elif average > 80 and average < 90:
  letterGrade = 'B'
  passed = True
elif average > 70 and average < 80:
  letterGrade = 'C'
  passed = True  
else:
  letterGrade = 'D or F'
  passed = False  

if passed == True:
  print('Student has passed with a grade letter of',letterGrade, "and a score of",average) 
else: 
  print("Student has failed with a grade letter of",letterGrade,"and a score of",average )
