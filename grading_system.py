#program to output the grade using a function
marks=int(input("Enter your marks="))

def grading(marks):
    if (marks<=100) and (marks>=70):
        print("A")
    elif (marks<=69) and (marks>=60):
        print("B")
    elif (marks<=59) and (marks>=50):
        print("C")
    elif (marks<=49) and (marks>=40):
        print("D")
    elif (marks<=39) and (marks>=0):
        print("D")   
    else:
        print("Enter valid marks")

print(grading(marks))