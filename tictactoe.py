
def display_board():
    print("  1   2   3")

    for i in range(3):
        print(i + 1, board[i][0], "|", board[i][1], "|", board[i][2])

        if i < 2:
            print(" ---|---|---")


def check_winner():

    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return True

    # Check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False


def check_draw():
    for row in board:
        for cell in row:
            if cell == " ":
                return False

    return True


# Start the game
play_again = "yes"

while play_again == "yes":

    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    current_player = "X"

    while True:

        print("Player", current_player, "turn")
        display_board()

        try:
            position = int(input("Enter a position (1-9): "))

            if position < 1 or position > 9:
                print("Please enter a number between 1 and 9.")
                continue

        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        row = (position - 1) // 3
        col = (position - 1) % 3

        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("Position already occupied! Try again.")
            continue

        display_board()

        if check_winner():
            print("Player", current_player, "wins!")
            break

        if check_draw():
            print("The game is a draw!")
            break

        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

    play_again = input("Would you like to play again? (yes/no): ").lower()

    while play_again not in ["yes", "no"]:
        print("Please enter yes or no.")
        play_again = input("Play again? (yes/no): ").lower()

print("Thank you for playing!")
