bill_amount = float(input("Enter total bill amount: "))
paid_amount = float(input("Enter paid amount: "))

if paid_amount < bill_amount:
    due = bill_amount - paid_amount
    print("Customer Due Amount =", due)

elif paid_amount == bill_amount:
    print("Bill fully paid. No due amount.")

else:
    extra = paid_amount - bill_amount
    print("Extra amount paid =", extra)