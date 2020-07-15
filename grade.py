def netGrade(mark):
   grade = ""
   if (mark<60): 
       grade="F" 
   elif(mark>=60) and (mark<70):
       grade="D"
   elif(mark>=70) and (mark<80):
        grade="C"
   elif(mark>=80) and (mark<90):
        grade="B"
   else :
        grade="A"
  
   return grade
myGrade = int(input("Enter mark:"))

print (netGrade(myGrade))
