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

rps = [rock,paper,scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
rps = [rock,paper,scissors]
print("Your choice")
print(rps[user_choice])

print("Computer choice:")

computer_choice = random.randint(0,2)
print(rps[computer_choice])

if user_choice == 0:
    if computer_choice == 0:
        print("It's a draw")
    elif computer_choice == 1:
        print("You lose")
    elif computer_choice == 2:
        print("You won")
elif user_choice == 1:
    if computer_choice == 0:
        print("You won")
    elif computer_choice == 1:
        print("It's a draw")
    elif computer_choice == 2:
        print("You lose")
elif user_choice == 2:
    if computer_choice == 0:
        print("You lose")
    elif computer_choice == 1:
        print("You won")
    elif computer_choice == 2:
        print("It's a draw")
