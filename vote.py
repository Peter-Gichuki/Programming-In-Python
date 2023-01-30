#program to check if a person is eligible to vote
age=int(input("Enter your age="))
citizenship=input("Enter the nationality=").lower() #(string methods) to allow a user enter the value in any form of lowercase or uppercase 
if age>=18 and  citizenship=="kenyan":
    print("Eligible to vote")
else:
    print("Not eligible to vote")
