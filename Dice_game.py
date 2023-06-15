#DICE GAME

import random

print("Welcome to the Dice game")

ready = input("\nAre you ready?: ")

if ready.lower() == "yes":
    player_name = input("\nPlease enter your name: ")
    player_score = 0
    CPU_score = 0
# first to 30 wins
while player_score < 30 and CPU_score <30 :
    print(input("Press ENTER to roll your dice: "))
    player_roll  = random.randint(1, 6)
    print(f"{player_name} rolled {player_roll}")
    player_score += player_roll

    print(input("CPU's turn. Press ENTER to roll the dice: "))
    CPU_roll = random.randint(1, 6)
    print(f"CPU rolled {CPU_roll}")
    CPU_score += CPU_roll

print("\nGAME OVER")
print(f"{player_name} scored: {player_score}")
print(f"CPU scored: {CPU_score}")

if player_score == CPU_score:
    print("Its a tie, LAST ROLL! Highest number wins!")
    print(input("Press ENTER to roll your dice: "))
    player_roll = random.randint(1, 6)
    print(f"{player_name} rolled {player_roll}")
    player_score += player_roll

    print(input("CPU's turn. Press ENTER to roll the dice: "))
    CPU_roll = random.randint(1, 6)
    print(f"CPU rolled {CPU_roll}")
    CPU_score += CPU_rollyes



if player_score > CPU_score:
    print(f"FAITALITY, {player_name} WINS")
elif player_score < CPU_score:
    print("TAKE THE L, CPU WINS")
