import random
random_int = random.randint(1, 100)
print(random_int)

rand_float = random.random()
print(rand_float)

# Heads or tails

random_int = random.randint(1, 2)
print(random_int)
if random_int == 1:
    print("Heads")
else:
    print("Tails")

# 2. Bank Random bill
name = input("Enter the list of members")
name_list = name.split(',')
no_of_mem = len(name_list)
random_per = random.randint(0, no_of_mem)
bill_mem = name_list[random_per]
print(f"The bill amount should be paid by {bill_mem}")

# print(name_list[10])

# Treasure Map
row1 = ["😀","😃","😄"]
row2 = ["🧑‍","🙇","👩‍"]
row3 = ["🚴‍", "🤸","👩‍"]
map = [row1,row2,row3]
print(f"{row1}\n, {row2}\n, {row3}\n")
