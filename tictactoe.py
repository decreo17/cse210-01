'''
Tic-Tac-Toe
Author: Dhener Trinidad
'''
"""
todo: 
    Fix the if statement for col to check the last item index instead of the last item itself
    add the ability to input
    add the player 2
    add the battle result 
"""

def create_board(size):
    """This will create a list which will be to create the initial interface"""
    board = []
    for s in range(size):
        board.append(s + 1)
    return board

def display_game(board, size):
    """This will serve as the interface of the game"""
    lines = list(divide_chunks(board, int(size ** 0.5)))
    for row in lines:
        for col in row:
            if (str(col) != str(row[len(row)-1])):
                print('{:0>2}'.format(col), end = " | ")
            else:
                print('{:0>2}'.format(col))
        if( str(row) != str(lines[len(lines)-1])):
            for col in row:
                if (str(col) != str(row[len(row)-1])):
                    print(end = "- + ")
                else:
                    print(" - ")   

def divide_chunks(l, n):
    """This will divide the list(l) by the number provided (n)"""
    for i in range(0, len(l), n): 
        yield l[i:i + n]

def main():
    #list = [1,2,3," x "," x "," x ",7,8,9] #for testing
    dimension = 3 #this will be an input in the final output
    size = dimension * dimension
    board = create_board(size)
    #board = list #for testing
    display_game(board, size)

if __name__ == "__main__":
    main()
