def board_to_string(board):
    result = ""

    for row in board:
        # counter = 0
        for element in row:

            result += element + "|"

            # if counter < 2:
            #     result += "|"
            # counter += 1
        result = result[0:-1]
        result += "\n"
    return result 

baba = [["X", "O", "#"],
        ["O", "X", "#"],
        ["#", "O", "X"]]
print(board_to_string(baba))