#rock paper scissors game 

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
---'    ____)____
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
game_images=[rock,paper, scissors]
users_choice=int(input("what do u choose ? type 0 for rock , 1 for paper , 2 for scossor: \n"))

if users_choice>=0 and users_choice<=2:
    print(game_images[users_choice])

computer_choice=random.randint(0,2)
print("computer chose:")
print(game_images[computer_choice])

if users_choice>=3 or users_choice<0:
    print("u type invalid number.you lose!")
elif users_choice==0 and computer_choice==2:
    print("you wins!")
elif computer_choice==0 and users_choice==2:
    print("you lose!")
elif computer_choice>users_choice:
    print("you loose!")
elif users_choice>computer_choice:
    print(" u win")
elif computer_choice==users_choice:
    print("its a draw!")
