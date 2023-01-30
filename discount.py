amount_purchased=float(input("Enter the amount="))
discount=5/100*amount_purchased
total_pay=amount_purchased-discount
if(amount_purchased>=1000):
    print("The total pay is=", total_pay, "your discount is=", discount)
else:
   print("The total pay is", amount_purchased)
