import re

file_name = "Day4/Day4Input.txt"

with open(file_name) as file:
    ### Setting up the game

    boards = []
    rolled = file.readline().strip().split(',')  # A list of all the numbers rolled


    # Loading up all the boards

    temp_board = []

    for line in file:
        if line != '\n':
            line = re.sub("\s+", "-", (line.strip()))
            temp_board.append(line.split('-'))

        if len(temp_board) == 5:
            boards.append(temp_board)
            temp_board = []


    ### Playing the game and choosing a winner

    # Defining a function to check for a winner

    def win_check():
        """Checks the winner by checking all rows and columns for one composed entirely out of 'X'"""

        for board in boards:
            rows = []
            columns = []

            for board_index in range(len(boards)):
                board = boards[board_index]
                temp = [[row[i] for row in board] for i in range(len(board[0]))]
                columns.append(temp)

                for column in temp:
                    if column == ["X" for _ in range(5)]:
                        return (board_index + 1)

                temp = [row for row in board]
                rows.append(temp)

                for row in temp:
                    if row == ["X" for _ in range(5)]:
                        return (board_index + 1)

            return 0

    # Marking all the rolled numbers until a winner emerges

    # r/badcode material coming up...

    while boards:
        winner = 0
        for rolled_number in rolled:
            for board in boards:
                for line in board:
                    for board_number in line:
                        if board_number == rolled_number:
                            line[line.index(board_number)] = "X"
                            winner = win_check()

                            if winner != 0:
                                break
                        if winner != 0:
                            break
                    if winner != 0:
                        break
                if winner != 0:
                    break
            if winner != 0:
                break

        # Eliminating the winning board and starting again to find the last board to win

        boards.pop(winner-1)

    ### Figuring out the score of the winning board

    # Calculating the score

    winning_board = board

    score = ((sum([int(number) for row in winning_board for number in row if number != "X"])) * int(rolled_number))


# Printing the score and board along with it

print(f"\nWinning Board Number: {winner}\n")
print(*winning_board, sep='\n')
print(f"\nWinning Board Score: {score}\n")
