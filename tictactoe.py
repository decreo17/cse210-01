'''
Tic-Tac-Toe
Author: Dhener Trinidad
'''
"""
Part of the codes were from source: https://geekflare.com/tic-tac-toe-python-code/ and solution
                                    https://www.geeksforgeeks.org/print-colors-python-terminal/
"""
"""
todo: 
    add input validation
    do not allow to override the current input
"""

def make_move(player, board):
    square = int(input(f"{player}'s turn, choose (1-{len(board)}): "))
    board[square - 1] = player

def is_draw(board):
    """This will check if all is string, then it's a draw"""
    #print(f"this is the board: {board}")
    if all([isinstance(item, str) for item in board]):
        print("Draw!")
        return True
    return False
 
def is_player_win(player, board, dimension):
    win = None
    board = list(divide_chunks(board, dimension))
    player = player.strip()
    n = len(board)
    
    # checking rows
    for i in range(n):
        win = True
        for j in range(n):
            if str(board[i][j]).strip() != player.strip():
                win = False
                break
        if win:
            print(f"{player} win!")
            return win
    # checking columns
    for i in range(n):
        win = True
        for j in range(n):
            if str(board[j][i]).strip() != player.strip():
                win = False
                break
        if win:
            print(f"{player} win!")
            return win
    # checking diagonals
    win = True
    for i in range(n):
        if str(board[i][i]).strip() != player.strip():
            win = False
            break
    if win:
        print(f"{player} win!")
        return win

    win = True
    for i in range(n):
        if str(board[i][n - 1 - i]).strip() != player.strip():
            win = False
            break
    if win:
        print(f"{player} win!")
        return win
    return False

def next_player(player):
    if player == "" or player == "O":
        return "X"
    else:
        return "O"

def create_board(size):
    """This will create a list which will be to create the initial interface"""
    board = []
    for s in range(size):
        board.append(s + 1)
    return board

def display_game(board, dimension):
    """This will serve as the interface of the game"""
    lines = list(divide_chunks(board, dimension))
    for row in lines:
        counter = 0
        counter_2 = 0
        for col in row:
            counter += 1
            if counter != dimension:
                #print('{:0>2}'.format(col), end = "|")
                print(col, end = "|")
            else:
                #print('{:0>2}'.format(col))
                print(col)
        if str(row) != str(lines[len(lines)-1]):
            for col in row:
                counter_2 += 1
                if (counter_2 != dimension):
                    print(end = "-+")
                else:
                    print("-")   

def divide_chunks(l, n):
    """This will divide the list(l) by the number provided (n)"""
    for i in range(0, len(l), n): 
        yield l[i:i + n]

def main():
    #list = [" X ", " X ", " X ", 4, " X ",6,7, " X ",9] #for testing
    #board = list #for testing
    #print(is_player_win(" X ", board, 3))

    dimension = 3#int(input('Choose the dimension (3-9): '))
    size = dimension * dimension
    board = create_board(size)
    player = next_player("")
    #display_game(board, dimension)

    while not (is_player_win(next_player(player), board, dimension) or is_draw(board)):
        display_game(board, dimension)
        make_move(player, board)
        player = next_player(player)

    display_game(board, dimension)
    print("Good game. Thanks for playing!") 

if __name__ == "__main__":
    main()
