class Student:
  def __init__(self, name:str, assignment:float, midtermScore:float, finalExamScore:float):
    self.name = name
    self.assignment = assignment
    self.midtermScore = midtermScore
    self.finalExamScore = finalExamScore

  def CalculateFinalGrade (self):
    finalGrade = (self.assignment + self.midtermScore + self.finalExamScore) /3

    if finalGrade >= 90:
      return "A"
    elif 80 <= finalGrade < 90:
      return "B"
    elif 70 <= finalGrade < 80:
      return "C"
    elif 60 <= finalGrade < 70:
      return "D"
    else:
      return "F"
 
    

  def output(self):
    return f"Student: {self.name} \nFinalGrade: {self.CalculateFinalGrade()}"
  
  def __str__(self):
      return self.output()

name = input("Enter your name: ")
try:
  assignment = float(input("Enter the assignment marks: "))
  midtermScore = float(input("Enter your midterm scores: "))
  finalExamScore = float(input("Enter the end of term examination marks: "))


  learner = Student(name, assignment, midtermScore, finalExamScore)  
  print(learner)

except ValueError:
  print( "Oops. Invalid input!")
  

  