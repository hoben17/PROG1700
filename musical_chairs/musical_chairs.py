# Author: Adam Hoben
# Student ID: W0184019
# Course: PROG 1700
# Date: November 18, 2026
# Version 1.0

import random

# Global Varibles
players = []
eliminated_players = []
num_players = 0
rounds = 1

print("Welcome to Musical Chairs")
print("IF YOU DO NOT GET A CHAIR AFTER A ROUND YOU ARE ELIMINATED")
print("__________________________________________________________")
while True:
    try:
        num_players = int(input("Number of players:"))
        if num_players >= 2:
            break
        else:
            print("Error: Enter a valid number (Musical Chairs requires at least 2 players)")
    except ValueError:
        print("Error: Enter a valid number!")
while len(players) < num_players:
    player_name = input("Enter player name: ").strip()
    if player_name == "":
        print("Error: name can not be blank")
    elif player_name in players:
        print("Name already exists, Please choose another one")
    else:
        players.append(player_name)
        print(f"{player_name} Successfully Registered!")

print("\nGame Starting")
print("One player will be eliminated at the end of each round.")
print("The last player with a chair wins!")

while len(players) > 1:
    chairs = len(players) - 1
    print("\n-------------------------------------------")
    print(f"Round: {rounds}")
    print(f"Number of Players: {len(players)}")
    print(f"Number of Chairs: {chairs}")
    print("\nActive Players:")
    for p in players:
        print(p)

    input("\nMusic is playing.....Press enter to stop.")

    # Randomally select a player
    eliminated = random.choice(players)

    #Remove the player and Record elimination
    players.remove(eliminated)
    eliminated_players.append(eliminated)

    print(f"\n{eliminated} has been eliminated")
    print(f"Remaining Players: {len(players)}")

    rounds += 1

# Display final results
print("\n=========================================")
print("Game Over")
print("\n=========================================")

print(f"Winner: {players[0]}")
print(f"Rounds Played: {rounds - 1}")

