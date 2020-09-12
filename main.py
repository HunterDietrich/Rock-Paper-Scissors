import random
#Project Planning
#2 Players
#1) ask player for their choice
#chooses either rosk, paper, scissors
#2) computer randomly makes choice
#3) printing both inputs
#4) Outputting/Comparing who won!
#paper beats rock
#scissors beats paper
#rock beats scissors

print("***WELCOME TO ROCK PAPER SCISSORS SHOWDOWN***")

choices = ["rock", "paper", "scissors"]

player_choice = input("Choose rock, paper, scissors: \n")

while player_choice not in choices:
    print(f"Player Choice: {player_choice}")
    player_choice = input("Not Valid, Please choose rock, paper, scissors: \n")
print(f"Player Choice: {player_choice}")
    
comp_choice = random.choice(choices)
print(f"Computer Choice: {comp_choice}")


if player_choice == comp_choice:
    print("**********Tie!***********")
else:
    if player_choice == "rock":
        if comp_choice == "paper":
            print("Computer Wins!")
        else:
            print ("Player Wins!")
