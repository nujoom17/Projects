import random

while True:
   liz=["rock","paper","scissors"]
   computer=random.choice(liz)
   player=None
   while player not in liz:
    player = input("rock, paper or scissors?").lower()
   if computer == player:
       print(f"com:{computer} \n player: {player} \n It's a tie")
   elif player == "rock":
       if computer == "paper":
           print(f"com:{computer} \n player: {player} \n You lose")
       if computer == "scissors":
           print(f"com:{computer} \n player: {player} \n You win")
   elif player == "paper":
       if computer == "scissors":
           print(f"com:{computer} \n player: {player} \n You lose")
       if computer == "rock":
           print(f"com:{computer} \n player: {player} \n You win")
   elif player == "scissors":
       if computer == "papers":
           print(f"com:{computer} \n player: {player} \n You win")
       if computer == "rock":
           print(f"com:{computer} \n player: {player} \n You lose")
   play_a = input("do you want to play again Y/N?").lower()
   if play_a not in ["yes","y"]:
       break

print("byee")











