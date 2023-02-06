subject1=int(input("Enter the marks for subject 1="))
subject2=int(input("Enter the marks for subject 2="))
subject3=int(input("Enter the marks for subject 3="))
average=(subject1+subject2+subject3)/3
print("Average marks=", average)
if (average>=70) and (average<100):
    print("Grade=A")
elif (average>=60) and (average<=69):
    print("Grade=B")
elif (average>=50) and (average<=59):
    print("Grade=c")
elif (average>=40) and (average<=49):
    print("Grade=D")
elif (average>=0) and (average<=39):
    print("Grade=E")