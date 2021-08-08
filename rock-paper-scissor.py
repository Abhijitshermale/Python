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
game_img=[rock,scissors,paper]
inp=int(input("What do you chose ? 0 for rock,1 for paper and 2 for scissors"))
print(game_img[inp])

rps_random=random.randint(0,2)
print("Computer Choice",game_img[rps_random])

if(inp>=3 and inp<0):
  print("Invalid Choice")
elif(inp==rps_random):
  print("Tie")
elif(inp>rps_random):
  print("You Loss")
elif(inp<rps_random):
  print("You Win")

