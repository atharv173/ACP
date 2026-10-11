
while True:
    try:
        bill = float(input("Enter the total shopping bill: "))
        if bill > 0:
            break
        print("Bill must be greater than 0!")

    except ValueError:
        print("Please enter a valid number!")

while True:
    try:
        discount = float(input("Enter discount percentage: "))
        if 0 <= discount <= 100:
            break
        print("Discount must be between 0 and 100!")

    except ValueError:
        print("Please enter a valid number!")

while True:
    try:
        people = int(input("Enter number of people: "))
        if people > 0:
            break
        print("Number of people must be greater than 0!")

    except ValueError:
        print("Please enter a valid whole number!")

discount_amount = bill * discount / 100
final_bill = bill - discount_amount
per_person = final_bill / people

print("Original Bill:", bill)
print("Discount Amount:", discount_amount)
print("Final Bill:", final_bill)
print("Each Person Pays:", round(per_person, 2))