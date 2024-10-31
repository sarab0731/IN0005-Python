import random

# Function to prompt a player to make a guess for the sum of the dice
def make_guess(player_name):
    return int(input(f"{player_name}, make your guess: "))

# Function to print the graphical representation of a dice face based on its value
def print_diceface(value):
    faces = {
        1: ["     ",
            "  .  ",
            "     "],
        2: [".    ",
            "     ",
            "    ."],
        3: [".    ",
            "  .  ",
            "    ."],
        4: [".   .",
            "     ",
            ".   ."],
        5: [".   .",
            "  .  ",
            ".   ."],
        6: [".   .",
            ".   .",
            ".   ."]
    }
    
    for face in faces[value]:
        print(face)

# Main code where the game logic is implemented

print("The aim of this game is to be the best at guessing the sums of three dice throws... You all have 5 lives each, and whoever lasts till the end is the winner!", end="\n\n")

# Generate a list of player names 1 through 6
players = [f"Player {i+1}" for i in range(6)]
# Initialize each player's remaining guesses to 5
guesses = {player: 5 for player in players}

# Main game loop, continues until only 1 or 0 players left
while len(players)> 1:
    round_guesses = {}
    # Loop through each player to get their guesses for the current round
    for player in players:
        if guesses[player] > 0:
            guess = make_guess(player)
            round_guesses[player] = guess

    # Roll three dice and calculate their sum
    value_1 = random.randint(1, 6)
    value_2 = random.randint(1, 6)
    value_3 = random.randint(1, 6)
    
    roll_result= value_1 + value_2 + value_3

    # Print the graphical representation of each dice face
    print_diceface(value_1)
    print()
    print_diceface(value_2)
    print()
    print_diceface(value_3)
    print()

    print(f"The sum of the dice is: {roll_result}")

    # Check each player's guess against the roll result and update their guesses accordingly
    for player, guess in round_guesses.items():
        if guess == roll_result:
            print(f"{player} guessed correctly!")
            print()
        else:
            guesses[player] -= 1
            print(f"{player}'s guess was incorrect. You have {guesses[player]} guesses left.")
            print()

    # Remove players who have run out of guesses from the active player list
    players = [player for player in players if guesses[player] > 0]

    # Declare the winner or indicate if there's no winner
if len(players) == 1:
        print(f"{players[0]} is the winner!")
else:
        print("No winner. All players are out of guesses.")
        






























