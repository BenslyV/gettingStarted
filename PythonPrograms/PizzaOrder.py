print("Welcome to Pizza Delivery")
print("Pizza rates are S 100, M 200 L 300")
size=input("Which Size You Want. Small 20, Medium 50 Large 100 S M L")
size=size.lower()
add_pep=input("Do ypu want to add Pep. Additional 50 you have to pay. Yes or No")
add_pep=add_pep.lower()
add_cheese=input("Want Cheese. Additional 50 . Y N")
add_cheese=add_cheese.lower()
if size==str("s"):
    bill=100
elif size==str("m"):
    bill=200
else:
    bill=300
bill_amount=bill
if add_pep==str("yes"):
    bill_amount=bill+50
else:
    bill_amount=bill
if add_cheese==str("y"):
    bill_amount=bill_amount+50
else:
    bill_amount=bill_amount
print(f"\nYour Bill amount is RS.{bill_amount}")