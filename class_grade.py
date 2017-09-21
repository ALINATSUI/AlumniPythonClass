#class activity:

#if student gets 90 or higher: they get an A
#if student gets 80 or above and less than 90: they get a B
#if student gets 70 or more and less than 80: they get a C
#if student gets 55 or above: and less than 70 they get a D
#Any grade lower than 55 is F

grade =int(input('>> '))
#student_grade = number
#A: 90-99
#B: 80-89
#C: 70-79
#D: 55-69
#F: <55

if(grade>=90 and grade <=99):
    print(f"The student's grade is: A")
elif(grade>=80 and grade <=89):
    print(f"The student's grade is: B")
elif(grade>=70 and grade <=79):
    print(f"The student's grade is: C")
elif(grade>=55 and grade <=69):
    print(f"The student's grade is: D")
else:
    print(f"The student's grade is: F")
