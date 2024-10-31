import random

# Function to print the game board with player positions
def print_board(P, Q):
    # Initialize the game board with empty cells
    board = [["|___|", "|___|", "|___|", "|___|", "|___|", "|___|", "|___|", "|___|"],
             ["|___|", "|___|", "|___|", "|___|", "|___|", "|___|", "|___|", "|___|"],
             ["|___|", "|___|", "|___|", "|___|", "|___|", "|___|", "|___|", "|___|"],
             ["|___|", "|___|", "|___|", "|___|", "|___|", "|___|", "|___|", "|___|"],
             ["|___|", "|___|", "|___|", "|___|", "|___|", "|___|", "|___|", "|___|"],
             ["|___|", "|___|", "|___|", "|___|", "|___|", "|___|", "|___|", "|___|"],
             ["|___|", "|___|", "|___|", "|___|", "|___|", "|___|", "|___|", "|___|"],
             ["|___|", "|___|", "|___|", "|___|", "|___|", "|___|", "|___|", "|___|"]
            ]

    # Place player P's token on the board
    if P == Q:
        board[P[0]][P[1]] = "|P_Q|"
    else:
        board[P[0]][P[1]] = "|_P_|"
        board[Q[0]][Q[1]] = "|_Q_|"

    # Print the board
    for row in board:
        print("".join(row))

# Function to print the face of a dice given its value
def print_diceface(value):
    # Mapping of dice values to their corresponding faces
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
    
    # Print the face of the dice with the given value
    for face in faces[value]:
        print(face)
        
        
# Function to handle player's move
def player_move(player_turn, dice_value, player_position):
    if player_turn:
        # Print the face of the rolled dice
        print_diceface(dice_value)
        # Check if player is at the starting row and within the board range
        if player_position[0] == 0 and player_position[1] <= 5:
            # If the dice value is greater than the remaining steps to the finish line
            if dice_value > player_position[1]:
                print(f"Invalid move - need dice value of less than or equal to {player_position[1]}")
            else:
                # Move the player
                player_position[1] -= dice_value
        else:
            # Movement for other areas of the board
            while dice_value > 0:
                if player_position[0] % 2 == 0:  # Even row
                    if player_position[1] == 0:
                        player_position[0] -= 1
                        dice_value -= 1
                    elif 1 <= player_position[1] <= 7:
                        player_position[1] -= 1
                        dice_value -= 1
                    else:
                        print("Error")
                elif player_position[0] % 2 == 1:  # Odd row
                    if player_position[1] == 7:
                        player_position[0] -= 1
                        dice_value -= 1
                    elif 0 <= player_position[1] <= 6:
                        player_position[1] += 1
                        dice_value -= 1
                    else:
                        print("Error")
        # Switch player's turn
        return not player_turn
    else:
        return player_turn


# Function to check if a player has reached the finish line
def check_for_winner(player_position, current_player):
    if player_position == [0, 0]:
        print()
        print(f"Player {current_player} is the winner! ")
        return True

# Initialize players' positions
P_position = [7, 0]
Q_position = [7, 0] 

# Print game instructions and initial board
print("This is a two player game. Each round the player must roll a dice to determine the moves that player makes per round. Whoever gets to the finish line first is the winner!", end="\n\n")
print_board(P_position, Q_position)

GameOver = False


    
# Main game loop
while not GameOver:
    P_turn = True
    Q_turn = True
    # Player P's turn
    while P_turn:
        # Roll the dice for Player P
        P_dice = random.randint(1, 6)
        input("Player P's turn. Press enter to roll the dice")
        # Perform Player P's move
        P_turn = player_move(P_turn, P_dice, P_position)
        # Print the updated board
        print_board(P_position, Q_position)
        # Check for a winner after Player P's turn
        if check_for_winner(P_position, "P"):
            GameOver = True
            break
    #if Player P wins, the main game loop is exited before entering player Q's loop.
    if GameOver ==True:
        break
    
    # Player Q's turn
    while Q_turn:
        # Roll the dice for Player Q
        Q_dice = random.randint(1, 6)
        input("Player Q's turn. Press enter to roll the dice")
        # Perform Player Q's move
        Q_turn = player_move(Q_turn, Q_dice, Q_position)
        # Print the updated board
        print_board(P_position, Q_position)
        # Check for a winner after Player Q's turn
        if check_for_winner(Q_position, "Q"):
            GameOver = True
            break


    
    
    







    
    
    