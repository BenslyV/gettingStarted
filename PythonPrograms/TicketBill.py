age = int(input("Enter the age"))
bill=0
if age<70:
    if age < 5:
        print("Pay 30 rs for ticket")
        bill=30
    elif age <= 5:
        print("Pay 50 rs for ticket")
        bill=50
    elif 18 <= age <= 70:
        print("Pay Rs 100 for ticket")
        bill=70
    want_photo= input("Do you want the Photo. 50 per photo . Yes or No\n")
    wp=want_photo.lower()
    cond="yes"
    if wp==str(cond):
        totat_bill = 50+bill;
        print(f"You have to Pay Rs {totat_bill}")

    else:
        print(f"You total bill is Rs {bill}")
else:
    print("You are not allowed")