# Create an empty 3x3 game board
board = [['_','_','_'],
         ['_','_','_'],
         ['_','_','_']
        ]

# Display the initial empty board
for i in range(3):
    for j in range(3):
        print(board[i][j], end = " ")
    print()
print()

# Game logic
current_player = 'X'  # Initialize player X as the starting player
GameOver = False  # Initialize the game state as not over

# Run the game loop until the game is over
while not GameOver:
    print(f"Player {current_player}'s turn.")
    row = int(input("Enter row (1, 2, or 3): "))  # Get user input for row
    col = int(input("Enter column (1, 2, or 3): "))  # Get user input for column

    # Check if the selected spot on the board is empty
    if board[row-1][col-1] == '_':
        board[row-1][col-1] = current_player  # Place the player's symbol on the board

        # Display the updated board
        for i in range(3):
            for j in range(3):
                print(board[i][j], end = " ")
            print()
        print()

        # Check for a win in rows, columns, or diagonals
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] == current_player or board[0][i] == board[1][i] == board[2][i] == current_player:
                print(f"Player {current_player} wins!")
                GameOver = True
                break

        if board[0][0] == board[1][1] == board[2][2] == current_player or board[0][2] == board[1][1] == board[2][0] == current_player:
            print(f"Player {current_player} wins!")
            GameOver = True
            break

        # Check for a tie
        is_tie = True
        for row in board:
            for cell in row:
                if cell == '_':
                    is_tie = False
                    break
            if not is_tie:
                break

        # If it's a tie, end the game
        if is_tie:
            print("It's a tie! Game over.")
            GameOver = True
            break

        # Switch players for the next turn
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'
    else:
        print("That spot is already taken. Try again.")  # If the spot is already filled, prompt for another move


