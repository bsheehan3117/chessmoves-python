'''
    CS5001
    Spring 2023
    HW3

    Brendan Sheehan

    This tests the can_rook_move , can_bishop_move,
    and can_queen_move functions
'''

from chessmoves import can_rook_move
from chessmoves import can_bishop_move
from chessmoves import can_queen_move

def test_various_moves():
    
    '''Function 

    Parameters:
    an original x coordinate
    an original y coordinate
    an x coordinate to be moved to
    a y coordinate to be moved to
        
    Return:
    true if chess piece can be moved to that coordinate
    false if chess piece cannot be moved to that coordinate

    Examples:
    rook:
    Input: (b, 5, b, 6) Output: true
    Input: (d, 5, a, 5) Output: true
    input: (b, 5, a, 7) Output: false
    bishop:
    Input: (c, 2, f, 5) Output: true
    Input: (a, 4, d, 1) Output: true
    Input: (a, 1, a, 5) Output: false
    queen:
    input: (f, 1, f, 7) Output: true
    input: (a, 3, f, 4) Output: false
    Input: (a, 4, d, 1) Output: true
    '''
    # rook tests
    test_can_rook_move("a", 4, "a", 5, True)
    test_can_rook_move("b", 4, "c", 5, False)
    test_can_rook_move("d", 3, "f", 3, True)

    # bishop tests
    test_can_bishop_move("a", 7, "a", 8, False)
    test_can_bishop_move("b", 5, "d", 7, True)
    test_can_bishop_move("f", 7, "b", 3, True)

    # queen tests
    test_can_queen_move("a", 1, "f", 6, True)
    test_can_queen_move("d", 5, "d", 1, True)
    test_can_queen_move("a", 1, "b", 8, False)

def test_can_rook_move(from_col, from_row, to_col, to_row, expected):
    actual = can_rook_move(from_col, from_row, to_col, to_row)
    print("Can a rook move from (", from_col, ",", from_row,
          ") to (", to_col, ",", to_row, ")  Expected = ", expected,
          "  Actual = ", actual)
 
def test_can_bishop_move(from_col, from_row, to_col, to_row, expected):
    actual = can_bishop_move(from_col, from_row, to_col, to_row)
    print("Can a rook move from (", from_col, ",", from_row, ") to (",
          to_col, ",", to_row, ")  Expected = ", expected,
          "  Actual = ", actual)
    
def test_can_queen_move(from_col, from_row, to_col, to_row, expected):
    actual = can_queen_move(from_col, from_row, to_col, to_row)
    print("Can a rook move from (", from_col, ",", from_row, ") to (",
          to_col, ",", to_row, ")  Expected = ", expected,
          "  Actual = ", actual)
    
def main():

    test_various_moves()

if __name__ == "__main__":
    main()
