'''
    CS5001
    Spring 2023
    HW3

    Brendan Sheehan

    These functions return whether the rook, bishop, and
    queen can move to certain coordinates
'''

def can_rook_move(from_col, from_row, to_col, to_row):

    '''
    Purpose: to determine whether the rook can move
    to certain coordinates
    ...
    Parameters: from_col, from_row, to_col, to_row
    ...
    Pre-condition: list-preconditions here
    The positions provided to the function are valid
    '''
    '''
    Examples:
    rook:
    Input: (b, 5, b, 6) Output: true
    Input: (d, 5, a, 5) Output: true
    input: (b, 5, a, 7) Output: false
    '''

    # converts case to upper for universal input use
    from_col = from_col.upper()
    to_col = to_col.upper()
    is_valid = False 

    # code to test whether move is possible
    
    if to_col >= from_col and to_row == from_row:
        is_valid = True      
    elif to_col == from_col and to_row > from_row:          
        is_valid = True  
    elif to_col <= from_col and to_row == from_row: 
        is_valid = True  
    elif to_col == from_col and to_row < from_row:
        is_valid = True 
        
    return (is_valid) 


def can_bishop_move(from_col, from_row, to_col, to_row):
    '''
    Purpose: to determine whether the bishop can move
    to certain coordinates
    ...
    Parameters: from_col, from_row, to_col, to_row
    ...
    Pre-condition: list-preconditions here
    The positions provided to the function are valid
    '''
    '''
    bishop:
    Input: (c, 2, f, 5) Output: true
    Input: (a, 4, d, 1) Output: true
    Input: (a, 1, a, 5) Output: false
    '''

    # converts input to upper case for universal use
    
    from_col = from_col.upper()
    to_col = to_col.upper()

    # converts input letter to ascii so that vars can be added
    to_col = str(ord(to_col))
    from_col = str(ord(from_col))
    to_col = int(to_col)
    from_col = int(from_col)
    to_row = int(to_row)
    from_row = int(from_row)

    # code to test whether move is possible
    x = 0
    
    is_valid = False
    while x < 8:
        temp_row_pos = from_row + x 
        temp_col_pos = from_col + x 

        if temp_col_pos == to_col and temp_row_pos == to_row:

            is_valid = True

            x = 8
            
        elif temp_col_pos - (x * 2) == to_col and temp_row_pos\
            - (x * 2) == to_row:
                is_valid = True
                x = 8
            
        elif temp_col_pos - (x * 2) == to_col and temp_row_pos == to_row:
            is_valid = True
            x = 8

        elif temp_col_pos == to_col and temp_row_pos - (x * 2) == to_row:
            is_valid = True
            x = 8 

        x = x + 1
    return (is_valid) 

        
def can_queen_move(from_col, from_row, to_col, to_row):
    '''
    Purpose: to determine whether the queen can move
    to certain coordinates
    ...
    Parameters: from_col, from_row, to_col, to_row
    ...
    Pre-condition: list-preconditions here
    The positions provided to the function are valid
    '''
    '''
    queen:
    input: (f, 1, f, 7) Output: true
    input: (a, 3, f, 4) Output: false
    Input: (a, 4, d, 1) Output: true
    '''

    # utilize code from previous functions as queen can do both moves
    
    is_valid = can_bishop_move(from_col, from_row, to_col, to_row)
    if is_valid is False:
        is_valid = can_rook_move(from_col, from_row, to_col, to_row)

    return (is_valid)


def main():

    print(can_queen_move(a,4,b,7))
if __name__ == '__main__':
    main()
