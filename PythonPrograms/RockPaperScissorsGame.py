import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
print(rock)
print(paper)
print(scissors)

user_choice=int(input("what do your choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))
computer_choice=random.randint(0,2)
print(f"Your choice {user_choice} and the computer choice {computer_choice}")
#print(computer_choice)
if user_choice==0:
    if computer_choice==0:
        print(" Both Equal")
    if computer_choice==1:
        print("You loose")
    if computer_choice==2:
        print("Your Loose")
if user_choice==1:
    if computer_choice==0:
        print(" You win")
    if computer_choice==1:
        print("Both Equal")
    if computer_choice==2:
        print("Your Loose")
if user_choice==2:
    if computer_choice==0:
        print(" You win")
    if computer_choice==1:
        print("You win")
    if computer_choice==2:
        print("Both Equal")
