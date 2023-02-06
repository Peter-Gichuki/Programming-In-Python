salary=float(input("Enter your salary="))
year_of_service=int(input("Enter the duration of work="))
if year_of_service>10:
    print("Your bonus amount=",10/100*salary)
elif year_of_service>=6 and year_of_service<=10:
    print("Your bonus amount=",8/100*salary)
elif year_of_service<6:
    print("Your bonus amount=",5/100*salary)
