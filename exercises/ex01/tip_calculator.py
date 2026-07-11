# create a tip calculator for splitting bills

print("Welcome to the tip calculator!")
bill_amount = float(input("What was the total bill? $"))
tips = int(input("How much tip would you like to give? 10, 12, 0r 15? "))
split_bill = int(input("How many people to split the bill? "))

tips_percent = tips / 100
bill_amount_percent = bill_amount * tips_percent
total_bill_amount = (bill_amount + bill_amount_percent) / split_bill

print(f"Each person should pay: ${round(total_bill_amount, 2)}")
