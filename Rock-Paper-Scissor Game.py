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
game_images = [rock, paper, scissors]
user_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choose == 0:
    print(rock)
elif user_choose == 1:
    print(paper)
elif user_choose == 2:
    print(scissors)
if user_choose >= 3 or user_choose < 0:
    print("You typed an invalid number. You lost!")
else:
    computer_choose = random.randint(0, 2)
    print("computer choose:")
    print(game_images[computer_choose])
if user_choose >= 3 or user_choose < 0:
    print()
elif user_choose == 0 and computer_choose == 2:
    print("You Win!")
elif user_choose == 2 and computer_choose == 0:
    print("You loose!")
elif user_choose > computer_choose:
    print("You Win!")
elif computer_choose > user_choose:
    print("You loose!")
elif computer_choose == user_choose:
    print("It's a draw!")
