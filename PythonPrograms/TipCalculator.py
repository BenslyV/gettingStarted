# 3.Tip Calculator

print("Welcome to the tip calculator")
total_bill = float(input("what was the total bill?"))
tip_percentage = input("What percentage tip would you like to give? 10 , 12, or 15 ? 12")
tip_plus_bill = float(total_bill)+(total_bill/int(tip_percentage))
no_of_people = int(input (" How many people to split the bill?"))
split_bill = float(tip_plus_bill/no_of_people)

print(f"Each person should pay $ {round(split_bill,2)}")
