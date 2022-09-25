#student name: Kevin Peng
#student number: 94742293

def checkColumn(puzzle: list, column: int):
    """ 
        param puzzle: a list of lists containing the puzzle 
        param column: the column to check (a value between 0 to 8)

        This function checks the indicated column of the puzzle, and 
        prints whether it is valid or not. 
        
        As usual, this function must not mutate puzzle 
    """
    # Set for holding entries of current column
    columnSet = set()

    # Iterate through column and add all elements to set
    for i in range(9):
        columnSet.add(puzzle[i][column])
    
    # Print if current column is valid or not
    print(f"Column {column} {getIsValidString(columnSet)}")


def checkRow(puzzle: list, row: int):
    """ 
        param puzzle: a list of lists containing the puzzle 
        param row: the row to check (a value between 0 to 8)

        This function checks the indicated row of the puzzle, and 
        prints whether it is valid or not. 
        
        As usual, this function must not mutate puzzle 
    """
    # Set for holding entries of current row
    rowSet = set()

    # Iterate through row and add all elements to set
    for i in range(9):
        rowSet.add(puzzle[row][i])
    
    # Print if current row is valid or not
    print(f"Row {row} {getIsValidString(rowSet)}")


def checkSubgrid(puzzle: list, subgrid: int):
    """ 
        param puzzle: a list of lists containing the puzzle 
        param subgrid: the subgrid to check (a value between 0 to 8)
        Subgrid numbering order:    0 1 2
                                    3 4 5
                                    6 7 8
        where each subgrid itself is a 3x3 portion of the original list
        
        This function checks the indicated subgrid of the puzzle, and 
        prints whether it is valid or not. 
        
        As usual, this function must not mutate puzzle 
    """
    # Set for holding entries of current subgrid
    subgridSet = set()

    # Get row and column ranges from helper function
    (rowRange, columnRange) = getSubgridIndices(subgrid)

    for row in rowRange:
        for col in columnRange:
            subgridSet.add(puzzle[row][col])

     # Print if current subgrid is valid or not
    print(f"Subgrid {subgrid} {getIsValidString(subgridSet)}")


def getSubgridIndices(subgrid: int):
    """  
        Helper function that returns row and column index ranges for any given subgrid
        Returns row and column index ranges as a tuple like so: (row, column)

        Example of mapping of subgrid number to column and row indices:
            0 -> col: 0,1,2 + row: 0,1,2
            1 -> col: 3,4,5 + row: 0,1,2
            2 -> col: 6,7,8 + row: 0,1,2
            3 -> col: 0,1,2 + row: 3,4,5
            4 -> col: 3,4,5 + row: 3,4,5
            5 -> col: 6,7,8 + row: 3,4,5
            and so on... 
    """

    # Calculate the starting row index as the floor division of subgrid number times 3 (times 3 because subgrid size is 3)
    rowStartIndex = (subgrid // 3) * 3
    rowIndices = range(rowStartIndex, rowStartIndex + 3)

    # Calculate the starting column index as subgrid number mod 3 times 3 (times 3 because subgrid size is 3)
    columnStartIndex = (subgrid % 3) * 3
    columnIndices = range(columnStartIndex, columnStartIndex + 3)

    return (rowIndices, columnIndices)

def getIsValidString(inputSet: set):
    """  
        Helper function that returns "valid" or "not valid" given the current set (column, row, or subgrid)
    """
    # The correct set of numbers for any given sudoku row, column, or subgrid
    correctSet = set(range(1, SIZE + 1))

    # Check validity of current set against correctSet and set isValidString for printing
    return "valid" if (inputSet == correctSet) else "not valid"


if __name__ == "__main__":
    test1 = [ [6, 2, 4, 5, 3, 9, 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5],
              [1, 4, 3, 8, 6, 5, 7, 2, 9],
              [9, 5, 8, 2, 4, 7, 3, 6, 1],
              [7, 6, 2, 3, 9, 1, 4, 5, 8],
              [3, 7, 1, 9, 5, 6, 8, 4, 2],
              [4, 9, 6, 1, 8, 2, 5, 7, 3],
              [2, 8, 5, 4, 7, 3, 9, 1, 6]
            ]
    test2 = [ [6, 2, 4, 5, 3, 9 , 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5 ],
              [6, 2, 4, 5, 3, 9 , 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5 ],
              [6, 2, 4, 5, 3, 9 , 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5 ]
            ]
    
    testcase = test1   #modify here for other testcases
    SIZE = 9

    for col in range(SIZE):  #checking all columns
        checkColumn(testcase, col)
    for row in range(SIZE):  #checking all rows
        checkRow(testcase, row)
    for subgrid in range(SIZE):   #checking all subgrids
        checkSubgrid(testcase, subgrid)