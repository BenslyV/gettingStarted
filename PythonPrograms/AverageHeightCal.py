print("Enter the heights of syudents")
heights=input("Heights are").split()
total_height=int(0)
no_of_stu=int(0)
current_max_number = heights[0]

for x in heights:
    print("X is"+x)
    x = int(x)
    print(type(x))

    no_of_stu=no_of_stu+1
    print(f"No of stu {no_of_stu}")
    total_height=total_height+x
    print(f"total height {total_height}")

    # Calculating the maximum value in the list

    for number in heights:
        if number > current_max_number:
            current_max_number = number

print(f"No of students are {no_of_stu} and their total height {total_height}")
ave_height=round(total_height/no_of_stu)
print(f"Average Height of students are {ave_height}")

print(f"Maimum value in the list {current_max_number}")